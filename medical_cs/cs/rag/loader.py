from langchain_community.vectorstores import FAISS

def load_vector_stores(embeddings, path='ollama_nomic_vs'):
    """
    Load a pre-saved vector stores.
    
    Args:
        embeddings (OllamaEmbeddings): The embedding used to load the vector store. It must be the same with the one used to prepopulate the saved vector store.
        path (Path like): The location of the pre-saved vector store. Default is `ollama_nomic_vs`.
        
    Returns:
        Object: Langchain FAISS vector stores
    """
    vector_store = FAISS.load_local(
        folder_path=path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )
    return vector_store