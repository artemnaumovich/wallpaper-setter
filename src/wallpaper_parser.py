
import requests
from bs4 import BeautifulSoup as bs



class WallpaperParser:

	HOST = 'https://wallpaperscraft.com'
	HEADERS = {
		'accept': '*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	}
	RESOLUTION_PAGE_URL = HOST + '/all/{resolution}'
	FIRST_PAGE_URL = HOST + '/catalog/{category}/{resolution}'


	def __init__(self, category, resolution):
		pass


	# precalc methods
	def precalc_number_of_pages(self):
		pass

	def precalc_number_of_pictures(self):
		pass


	# build methods
	def build_resolution_page_url(self):
		pass

	def build_page_by_number_url(self, number):
		pass

	def build_first_page_url(self):
		pass

	def build_last_page_url(self):
		pass


	# get methods
	def get_html(self, url):
		pass

	def get_soup(self, url):
		pass

	def download_picture(self, url):
		pass


	# additional
	def page_not_found(self, url):
		pass


	# api
	def get_random_picture(self):
		pass