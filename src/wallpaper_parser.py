
import requests
from bs4 import BeautifulSoup as bs



class WallpaperParser:

	HOST = 'https://wallpaperscraft.com'
	HEADERS = {
		'accept': '*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	}
	RESOLUTION_PAGE_URL = HOST + '/all/{resolution}'
	PAGE_URL = HOST + '/catalog/{category}/{resolution}/page{page_number}'


	def __init__(self, category, resolution):
		self.category = category
		self.resolution = resolution


	def precalc_number_of_pages(self):
		pass

	def precalc_number_of_pictures(self):
		pass


	def build_resolution_page_url(self):
		url = self.RESOLUTION_PAGE_URL.format(resolution=self.resolution)
		return url

	def build_page_url_by_number(self, number):
		url = self.PAGE_URL.format(category=self.category, resolution=self.resolution, page_number=number)
		return url

	def build_first_page_url(self):
		url = self.build_page_url_by_number(number=1)
		return url

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
