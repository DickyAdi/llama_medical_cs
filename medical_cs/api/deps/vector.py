from context.app_context import app_context

def get_vector_store():
    """
    FastAPI dependency injection getter for the vector store.
    
    Returns:
        Object: Langchain FAISS object
    """
    return app_context.vector_stores