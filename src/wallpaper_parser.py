
import requests
from bs4 import BeautifulSoup as bs



class WallpaperParser:

	HOST = 'https://wallpaperscraft.com'
	HEADERS = {
		'accept': '*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	}
	RESOLUTION_PAGE_URL = HOST + '/all/{resolution}'
	PAGE_URL = HOST + '/catalog/{category}/{resolution}/page{number}'


	def __init__(self, category, resolution):
		pass


	def precalc_number_of_pages(self):
		pass

	def precalc_number_of_pictures(self):
		pass


	def build_resolution_page_url(self):
		pass

	def build_page_by_number_url(self, number):
		pass

	def build_first_page_url(self):
		pass

	def build_last_page_url(self):
		pass


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


	def page_not_found(self, url):
		pass


	# api
	def get_random_picture(self):
		pass
