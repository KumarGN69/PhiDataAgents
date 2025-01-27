from custom_llm import LLMModel
from pydantic import BaseModel
from typing import Literal, Optional
from pprint import pprint
from ollama import Client
class Object(BaseModel):
  name: str
  confidence: float
  attributes: str

class ImageDescription(BaseModel):
  summary: str
  objects: list[Object]
  scene: str
  colors: list[str]
  time_of_day: Literal['Morning', 'Afternoon', 'Evening', 'Night']
  setting: Literal['Indoor', 'Outdoor', 'Unknown']
  text_content: Optional[str] = None

path = './image.JPG'

model= LLMModel()
client = model.getclientinterface()

generated_content = client.generate(
            model="llava",
            format=ImageDescription.model_json_schema(),
            images=[path],
            options = {"temperature": 0.0},
            prompt= ("Analyze this image and describe in specific detail what you see, including any objects,"
                    "the scene, colors and any text you can detect.")
        )
result = ImageDescription.model_validate_json(generated_content.response)
pprint(result)
