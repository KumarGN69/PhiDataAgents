import os
from dotenv import load_dotenv
# load the env variables
load_dotenv()
# Configurations for the model
LLM_MODEL_TO_USE = os.getenv("MODEL_NAME")
OUTPUT_FORMAT = "json"
MODEL_TEMPERATURE = 0.0

#Prompts for the task to be performed
TASK_TO_PERFORM = "What is the color of the sky at different times of a day?What are the reasons for it?"
SEARCH_STRING= " What happened on penultimate voyage as Ferreira ? "
SUMMARIZE_STRING = "Summarize the article"

RETRIEVED_RESPONSE = "Wilfred Dowman’s premature death in 1936 brought about Cutty Sark’s next move"

SEARCH_PROMPT = (f"Answer the user's query based on the provided context. "
          f"User's query is {SEARCH_STRING}. "
          f"Context: ")

SUMMARIZE_PROMPT = (f"Summarize based on the provided context. "
          f"User's query is {SUMMARIZE_STRING}. "
          f"Context: ")
#Instructions to the agents
WEBSITE = "https://www.rmg.co.uk/stories/topics/cutty-sark-greenwich-history"