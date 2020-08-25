
from general_parser import GeneralParser
import random

class WallpaperParser(GeneralParser):

	HOST = 'https://wallpaperscraft.com'
	RESOLUTION_PAGE_URL = HOST + '/all/{resolution}'
	PAGE_URL = HOST + '/catalog/{category}/{resolution}/page{page_number}'

	def __init__(self, category, resolution):
		self.category = category
		self.resolution = resolution
		self.number_of_pages = self.precalc_number_of_pages()
		self.number_of_pictures_on_page = self.precalc_number_of_pictures_on_page()
		self.number_of_pictures = self.precalc_number_of_pictures()

	def precalc_number_of_pages(self):
		first_page_url = self.build_first_page_url()
		soup = self.get_soup(first_page_url)
		pager = soup.find('div', class_='pager')
		if pager is None:
			number_of_pages = 1
		else:
			pager_list = pager.find('ul', class_='pager__list')
			pager_items = pager_list.find_all('li', class_='pager__item')
			last_item = pager_items[-1]
			last_item_classes = last_item.get('class')
			last_link = last_item.find('a', class_='pager__link')
			if 'pager__item_last-page' in last_item_classes:
				last_href = last_link.get('href')
				number_of_pages = int(last_href.partition('page')[-1])
			else:
				number_of_pages = int(last_link.get_text())
		return number_of_pages

	def precalc_number_of_pictures_on_page(self):
		first_page_url = self.build_first_page_url()
		picture_urls = self.get_picture_urls_on_page(first_page_url)
		number_of_pictures_on_page = len(picture_urls)
		return number_of_pictures_on_page

	def precalc_number_of_pictures(self):
		last_page_url = self.build_last_page_url()
		picture_urls_on_last_page = self.get_picture_urls_on_page(last_page_url)
		number_of_pictures_on_last_page = len(picture_urls_on_last_page)
		number_of_pictures = (self.number_of_pages - 1) * self.number_of_pictures_on_page + number_of_pictures_on_last_page
		return number_of_pictures

	def get_picture_urls_on_page(self, url):
		soup = self.get_soup(url)
		picture_list = soup.find('ul', class_='wallpapers__list')
		picture_items = picture_list.find_all('li', class_='wallpapers__item')
		picture_hrefs = [item.find('a', class_='wallpapers__link').get('href') for item in picture_items]
		picture_urls = [self.build_picture_page_url(href) for href in picture_hrefs]
		return picture_urls

	def get_picture_page_url_by_number(self, url, number):
		soup = self.get_soup(url)
		picture_urls = self.get_picture_urls_on_page(url)
		picture_url = picture_urls[number - 1]
		return picture_url

	def get_picture_download_url(self, url):
		soup = self.get_soup(url)
		item = soup.find('div', class_='wallpaper__placeholder')
		download_url = item.find('a').get('href')
		return download_url

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
		url = self.build_page_url_by_number(self.number_of_pages)
		return url

	def build_picture_page_url(self, href):
		url = self.HOST + href
		return url

	def request_is_correct(self, url):
		pass

	@classmethod
	def get_filters(cls):
		soup = cls.get_soup(url=cls.HOST)
		items = soup.find_all('div', class_='filters')
		
		categories_item = items[0]
		categories_links = categories_item.find_all('a', class_='filter__link')
		categories_hrefs = [link.get('href') for link in categories_links]
		categories = [href.partition('/catalog/')[-1] for href in categories_hrefs]

		resolutions_item = items[1]
		resolutions_list = resolutions_item.find_all('li', class_='filter')
		#resolutions_links = resolutions_item.find_all('a', class_='filter__link')
		resolutions_links = [element.find('a', class_='filter__link') for element in resolutions_list]
		resolutions_hrefs = [link.get('href') for link in resolutions_links]
		resolutions = [href.partition('/all/')[-1] for href in resolutions_hrefs]

		filters = {
			'categories': categories,
			'resolutions': resolutions
		}

		return filters

	def get_random_picture_url(self):
		picture_number = random.randint(1, self.number_of_pictures)
		page_number = (picture_number + self.number_of_pictures_on_page - 1) // (self.number_of_pictures_on_page)
		picture_number_on_page = picture_number - (page_number - 1) * self.number_of_pictures_on_page
		
		page_url = self.build_page_url_by_number(page_number)
		picture_page_url = self.get_picture_page_url_by_number(page_url, picture_number_on_page)
		download_url = self.get_picture_download_url(picture_page_url)
		#picture = self.download_picture(download_url)

		return download_url
