import requests
from bs4 import BeautifulSoup
from pprint import pprint
from phi.tools import Toolkit

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

            # Find all text on the page and print it out
            for script in soup(["script", "style"]):
                script.extract()

            text = soup.get_text()

            # Break into lines and remove leading/trailing whitespace from each line
            lines = (line.strip() for line in text.splitlines())

            # Break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

            # Drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)

            return text

# if __name__ == "__main__" :
#     scrape_tool = ScrapeTool(WEBSITE)
#     pprint(scrape_tool.getwebsitedata())