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
# SEARCH_STRING= " What happened on penultimate voyage as Ferreira ? "
SEARCH_STRING = "what did captain Wilfred Dowman do when he spotted the famous ship?"
SUMMARIZE_STRING = "Summarize the article"

SEARCH_PROMPT = (f"Answer the user's query based on the provided context. Context:")

SUMMARIZE_PROMPT = "Summarize based on the provided context. Context: "

# GRAPH_EXTRACT_PROMPT = (f"You are an experienced annotator.Extract all entities and the relationships and format the "
#                         f"output in JSON including the various events, activities, history from the content in")
GRAPH_EXTRACT_PROMPT = """
Input:
You are an expert in natural language processing. Your task is to analyze the given text and extract meaningful entities
, relationships between them, events related to them and history associated with them in a structured format. 
The extracted entities should include people, organizations, locations, events, objects, concepts, or other significant
elements mentioned in the text. For each identified entity, determine its type (e.g., Person, Organization, Location, 
Concept, Event, Object, History, Transactions, LifeEvents etc.). Then, extract relationships between these entities and describe 
them in a subject-predicate-object (SPO) format.

Output Format:
Return the extracted entities and relationships in a structured JSON format as follows 

{
  "Entities": [
    {"name": "Entity1", "type": "Type1"},
    {"name": "Entity2", "type": "Type2"},
    {"name": "Entity3", "type": "Type3"}
  ],
  "Relationships": [
    {"subject": "Entity1", "predicate": "RelationshipType", "object": "Entity2"},
    {"subject": "Entity2", "predicate": "RelationshipType", "object": "Entity3"}
  ],
  "Events": [
    {"subject": "Entity1", "predicate": "EventType", "object": "Entity2"},
    {"subject": "Entity2", "predicate": "EventType", "object": "Entity3"}
  ],
   "History": [
    {"subject": "Entity1", "predicate": "HistoryType", "object": "Entity2"},
    {"subject": "Entity2", "predicate": "HistoryType", "object": "Entity3"}
  ]
}
"""
#Instructions to the agents
WEBSITE = "https://www.rmg.co.uk/stories/topics/cutty-sark-greenwich-history"