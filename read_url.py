import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.website import WebsiteTools
from pprint import pprint
from webscrape import ScrapeTool


WEBSITE = "https://www.rmg.co.uk/stories/topics/why-sky-blue"
message = f"Read the full content without missing any line or word from the website "

# Load environment variables from .env file
load_dotenv()



# instantiate the Ollama object using phiData Ollama integration
llm = Ollama(
        id=os.getenv("MODEL_NAME"),
        name='Ollama',
        host= os.getenv("BASE_URL"),
        model= os.getenv("MODEL_NAME"),
        # format="json",
        temperature=0.0
        )

# Initialize the agent
website_agent = Agent(
    name="Website reader AI Agent",
    model = llm,
    tools=[WebsiteTools()],#custom tool
    description="You are an expert website reader. Scrape the full information from the website.",
    instructions=[message],
    show_tool_calls=True,
    markdown=False,
)

response = website_agent.run(
    message=message + f"{WEBSITE}",
    stream=False
)
print(type(response.content))
print(response.content)