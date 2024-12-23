import os
# Import LLM classes
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI
# from langchain_groq import ChatGroq
# from langchain_fireworks import ChatFireworks
# from langchain_ollama import ChatOllama

# Load environment variables from .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_llm(model_name, **kwargs):
    """
    Retrieve the appropriate LLM instance based on the provided model name.

    Args:
        model_name (str): The name of the model to initialize.
        **kwargs: Additional parameters for the LLM initialization.

    Returns:
        An instance of the specified LLM.

    Raises:
        ValueError: If the model name is not supported.
    """
    llm_classes = {
        "gemini-1.5-flash": ChatGoogleGenerativeAI,
        # "gpt-4o-2024-08-06": ChatOpenAI,
        # "llama-3.1-70b-versatile": ChatGroq,
        # "llama-v3-70b-instruct": ChatFireworks,
        # "llama3.1": ChatOllama
    }

    if model_name not in llm_classes:
        raise ValueError(f"Model '{model_name}' is not supported.")

    llm_class = llm_classes[model_name]
    return llm_class(model=model_name, **kwargs)