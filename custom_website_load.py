import requests
from bs4 import BeautifulSoup
from phi.tools import Toolkit
class WebScrapeTool(Toolkit):
    """
    This class defines a custom webscrape using phiData Toolkit
    --------------------------------------------------------
    Methods:
    getwebsitecontent() :
        args: None
        return: Return a document List of the text contexts from the website

    """
    def __init__(self,url:str):
        super().__init__(name="scrape tools")
        self.url = url

    def getwebsitecontent(self)->str:
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
            # find all paragraphs in the web content
            p_tags = soup.find_all('p')

            #Create and return a list of contents from scrapped from the website
            webcontent_list =[]
            for tag in p_tags:
                webcontent_list.append(tag.text)
            return webcontent_list
