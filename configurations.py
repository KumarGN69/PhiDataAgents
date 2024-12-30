import os
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
SEARCH_STRING= "How do astronomers at Royal Observatory Greenwich explain the color of the sky at sunrise?"

#Instructions to the agents
WEBSITE = "https://www.rmg.co.uk/stories/topics/why-sky-blue"