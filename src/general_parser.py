import requests
from bs4 import BeautifulSoup as bs

class GeneralParser:
	
	HEADERS = {
		'accept': '*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	}
	
	def get_html(self, url):
		resp = requests.get(url=url, headers=self.HEADERS)
		return resp

	def get_content(self, url):
		html = self.get_html(url)
		content = html.content
		return content

	def get_soup(self, url):
		content = self.get_content(url)
		soup = bs(content, 'html.parser')
		return soup
	
	def download_picture(self, url):
		picture = self.get_content(url)
		return picture
