import requests
from bs4 import BeautifulSoup as bs


class GeneralParser:
	
	HEADERS = {
		'accept': '*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	}
	
	@classmethod
	def get_html(cls, url):
		resp = requests.get(url=url, headers=cls.HEADERS)
		return resp

	@classmethod
	def get_content(cls, url):
		html = cls.get_html(url)
		content = html.content
		return content

	@classmethod
	def get_soup(cls, url):
		content = cls.get_content(url)
		soup = bs(content, 'html.parser')
		return soup
	
	@classmethod
	def download_picture(cls, url):
		picture = cls.get_content(url)
		return picture
