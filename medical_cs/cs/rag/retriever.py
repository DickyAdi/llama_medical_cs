def retrieve_context(query, vector_store, k=3):
    """
    Performing similarity search within the vector store based on the user query
    
    Args:
        query (str): User query to be search.
        vector_store (langchain FAISS object): The vector store used to find the context of the query.
        k (int): Number of context that should be retrieved. Default is 3
        
    Returns:
        str: A formatted string containing the k additional context.
    """
    return '\n'.join([f"{i+1}. {c.page_content}" for i, c in enumerate(vector_store.similarity_search(query=query))])