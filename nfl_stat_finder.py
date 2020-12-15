import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

class NFLStatFinder():
    def __init__(self):
        self.currentYear = datetime.today().year
        self.url_prefix = "https://www.pro-football-reference.com/teams/"
        self.url_suffix = "/" + str(self.currentYear) + ".htm"

    def find(self, team):
        scraping_url = self.url_prefix + team + self.url_suffix
        page = requests.get(scraping_url)

        soup = BeautifulSoup(page.content, 'lxml')

        # find by id
        # results = soup.find(id="ResultsContainer")
        # find by class
        # results = results.find_all('section', class_="card-content")
        # results = results.find('h2', class_='title')
        #summary = soup.find_all()
        #print(soup.prettify())
