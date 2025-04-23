from cs.rag.loader import load_vector_stores
from langchain_ollama import ChatOllama, OllamaEmbeddings
from cs.tools import agent


class AppContext:
    """
    Application-wide context manager for dependency injection.
    
    Attributes:
        vector_stores (Langchain FAISS object): The vector store used within the application.
        llm (ChatOllama object): The LLM used within the application.
        embeddings (OllamaEmbeddings object): The embeddings used to retrieve the context from RAG.
        llm_with_tools (Langchain LLM object): An LLM object binded with the tools to act as an agent.
        tools (list): List of agent tools which will be binded to the llm.
    """
    def __init__(self):
        self.vector_stores = None
        self.llm = None
        self.embeddings = None
        self.llm_with_tools = None
        self.tools = None
    def load_resources(self):
        """
        Loading all the necessary object for the application-wide context manager.
        """
        self.embeddings = OllamaEmbeddings(model='nomic-embed-text')
        self.vector_stores = load_vector_stores(self.embeddings)
        self.llm = ChatOllama(
            model = "llama3.2:3b-tool", temperature = 0
        )
        self.tools = [agent.check_schedule, agent.check_specialist_schedule, agent.validate_booking]
        self.llm_with_tools = self.llm.bind_tools(self.tools)

        
app_context = AppContext()