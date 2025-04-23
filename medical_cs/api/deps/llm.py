from context.app_context import app_context

def get_llm():
    """
    FastAPI dependency injection getter for the LLM.
    
    Returns:
        Object: The object of the LLM. In this case ChatOllama.
    """
    return app_context.llm

def get_llm_with_tools():
    """
    FastAPI dependency injection getter for the tools binded LLM.
    
    Returns:
        Object: The object of the LLM. In this case OllamaEmbeddings.
    """
    return app_context.llm_with_tools