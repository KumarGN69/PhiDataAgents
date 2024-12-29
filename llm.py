import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from configurations import LLM_MODEL_TO_USE, OUTPUT_FORMAT, MODEL_TEMP

class LLMModel:
    """
    This class defines the a custom model using Ollama
    --------------------------------------------------------
    Function getinstance() return the handle the model with specific parameters
    Takes no argument. For future this can be customize to pass the parameters to configure the llm
    returns the OllamaLLM model
    """
    def __init__(self):
        """constructor for the LLMModel class and populates the host, api key and the model to use"""
        load_dotenv()
        self.MODEL_URL = os.getenv("BASE_URL")
        self.API_KEY = os.getenv("API_KEY")
        self.MODEL_NAME = os.getenv("MODEL_NAME")
        # self.MODEL_NAME= "mistral"
        self.temperature = 0.0
    def getinstance(self):
        """Return the handle to the specific custom model"""
        return OllamaLLM(
            base_url=self.MODEL_URL,
            api_key=self.API_KEY,
            model=LLM_MODEL_TO_USE,
            format=OUTPUT_FORMAT,
            temperature=MODEL_TEMP
        )
