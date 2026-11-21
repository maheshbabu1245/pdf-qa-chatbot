import os
import chromadb
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

# load environment variable

load_dotenv()

# Initialize Groq client

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
    
)

# load embedding model
embeding_model = SentenceTransformer(
    "sentence-transformers/all-miniLM-L6-v2"
)

#initialize chromadb

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

# Extract text from Pdf

def extract_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    
    full_text = ""
    
    for page_number,page in enumerate(reader.pages,start=1):
        text = page.extract_text() or ""
        full_text +=f"\nPage{page_number}:\n{text}"
    return full_text
#splite text into chunks
def split_text(text,chunk_size=1000,overlap=150):
    chunks = []
    start = 0
    while start<len(text):
        chunk = text[start:start+chunk_size]
        if chunk.strip():
            chunks.append(chunk)
        start +=chunk_size-overlap
    return chunks

# genrate embeddings and strore in chromadb
def store_embeddings(chunks):
    collection = chroma_client.get_or_create_collection(
        name="pdf_qa"
    )

    embeddings = embeding_model.encode(
        chunks
    ).tolist()
    collection.upsert(
        ids=[
            f"chunk_{i}"
            for i in range(len(chunks))
                  
        ],
        documents=chunks,
        embeddings=embeddings
    )
    print("PDF embedding stored successfully:")
    
# Retrval relevent chunks
def retrieve_context(question):
    collection = chroma_client.get_collection(
        name="pdf_qa"
    )
    question_embedding = embeding_model.encode(
        question
    ).tolist()
    results = collection.query(
        query_embeddings = [question_embedding],
        n_results = min(4,collection.count())

    )
    context = "\n\n".join(
        results["documents"][0]
    )
    return context

#Ask question to LLM

def ask_question(question,context):
    system_prompt="""
    You are a PDF question answering assistant.
    Answer only using the provided PDF context.
    
    If the answer is not available in the context,
    say that the infromation is not available in
    the uploaded PDF.
    
    Do not invent information
    """
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role":"system",
                "content": system_prompt
                
            },
            {
                "role":"user",
                "content":f"""
                PDF Context:
                {context}
                Question:
                {question}
                """
                
            }
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

#Main applicaiton
if __name__=="__main__":
    pdf_path = input("enter your pdf path: ")
    print("\n Extracting pdf text...")
    pdf_text = extract_pdf_text(pdf_path)
    if not pdf_text.strip():
        raise ValueError("No readable text found in hte PDF.")
    print("Splitting text into chunks... ")
    chunks = split_text(pdf_text)
    print(f"Total chunks:{len(chunks)}")
    print("Generating embeddings.. ")
    store_embeddings(chunks)
    print("\nPDF is ready! Ask your quesions.")
    while True:
        question = input("\nAsk question (type exit to stop): ")
        if question.lower() =="exit":
            print("chatbot stopped.")
            break
        context = retrieve_context(question)
        answer = ask_question(question,context)
        print("\nAI Answer:")
        print(answer)