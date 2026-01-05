from langchain_ollama import OllamaEmbeddings # New import

def get_embedding_function():
    # Uses the modern langchain-ollama package
    return OllamaEmbeddings(model="nomic-embed-text")