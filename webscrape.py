import requests
from bs4 import BeautifulSoup
from pprint import pprint
from phi.tools import Toolkit
from configurations import WEBSITE
class ScrapeTool(Toolkit):

    def __init__(self,url:str,message:str):
        super().__init__(name="scrape tools")
        self.url = url
        self.message = message

    def getwebsitedata(self)->str:
        """Posts a get request to scrape a website using BeautifulSoup.
        Args:
            None
        Returns:
            str: Formatted output of the content of the website
        """
        response = requests.get(url=self.url)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve page. Status code: {response.status_code}")
        else:
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # fina all paragraphs in the web content
            p_tags = soup.find_all('p')
            # create a list of all web content
            web_content = []
            for tag in p_tags:
                web_content.append(tag.text)
            # append the paragraph contents into one large string
            web_text = ''.join(tag.text for tag in p_tags )
            # print(type(web_text))
            # print(web_text)
            return web_text

# if __name__ == "__main__" :
#     scrape_tool = ScrapeTool(WEBSITE,"")
#     # print(scrape_tool.getwebsitedata())
#     scrape_tool.getwebsitedata()