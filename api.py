from flask import Flask, request, jsonify
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Crear app Flask
app = Flask(__name__)

# --- 1. Cargar y procesar las páginas web ---
urls = [
    "https://aigenz.es/",
    "https://aigenz.es/servicios-de-inteligencia-artificial/",
    "https://aigenz.es/aplicaciones-con-inteligencia-artificial/",
    "https://aigenz.es/inteligencia-artificial-generativa-personalizada/",
    "https://aigenz.es/automatizaciones-inteligentes/"
]

# Cargar contenido HTML de las páginas
loader = WebBaseLoader(urls, headers={"User-Agent": "WebChatbotLangchain/1.0"})
documents = loader.load()

# Dividir contenido en chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs_chunked = text_splitter.split_documents(documents)

# Crear el vectorstore en memoria
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs_chunked, embeddings)

# Crear la cadena de QA
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Función principal del agente
def webGPT(pregunta: str) -> str:
    return qa_chain.run(pregunta)

# --- 2. Endpoint de API ---
@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json()
    pregunta = data.get("pregunta", "")
    respuesta = webGPT(pregunta)
    return jsonify({"respuesta": respuesta})

# --- 3. Ejecutar localmente ---
if __name__ == "__main__":
    app.run(debug=True)
