from custom_llm import LLMModel
from pydantic import BaseModel
from typing import Literal, Optional
from pprint import pprint
from ollama import Client
class Object(BaseModel):
    """Base model to capture the objects in an image for structured output"""
    name: str
    confidence: float
    attributes: str

class ImageDescription(BaseModel):
    """Base model to capture the description and contents of the image"""
    summary: str
    objects: list[Object]
    scene: str
    colors: list[str]
    time_of_day: Literal['Morning', 'Afternoon', 'Evening', 'Night']
    setting: Literal['Indoor', 'Outdoor', 'Unknown']
    text_content: Optional[str] = None


class CustomImageRead():
    """
    Read an image file and describe the contents, colors and detail out the contents
    Methods:
        readimage():
            args: None
            return: contents of the image as per the structured output ImageDescription
    """
    def __init__(self, **kwargs):
        self.model = LLMModel()
        self.image_path = kwargs.get("path")

    def readimage(self):
        """
        Read the contents and describe the image
        returns: contents of the image per the ImageDescription object
        """
        client = self.model.getclientinterface()

        generated_content = client.generate(
                    model=self.model.VISION_MODEL,
                    format=ImageDescription.model_json_schema(),
                    images=[self.image_path],
                    options = {"temperature": 0.0},
                    prompt= ("Analyze this image and describe in specific detail what you see, including any objects,"
                            "the scene, colors and any text you can detect.")
                )
        result = ImageDescription.model_validate_json(generated_content.response)

        return result

if __name__ == "__main__":
    image_contents = CustomImageRead(path="./image.jpg")
    pprint(image_contents.readimage())
