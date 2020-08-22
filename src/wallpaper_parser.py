
from general_parser import GeneralParser

class WallpaperParser(GeneralParser):

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
		pictures = self.get_picture_links_on_page(first_page_url)
		number_of_pictures_on_page = len(pictures)
		return number_of_pictures_on_page

	def precalc_number_of_pictures(self):
		last_page_url = self.build_last_page_url()
		picture_links_on_last_page = self.get_picture_links_on_page(last_page_url)
		number_of_pictures_on_last_page = len(picture_links_on_last_page)
		number_of_pictures = (self.number_of_pages - 1) * self.number_of_pictures_on_page + number_of_pictures_on_last_page
		return number_of_pictures

	def get_picture_links_on_page(self, url):
		soup = self.get_soup(url)
		picture_list = soup.find('ul', class_='wallpapers__list')
		picture_items = picture_list.find_all('li', class_='wallpapers__item')
		picture_links = [item.find('a', class_='wallpapers__link').get('href') for item in picture_items]
		return picture_links

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

	def page_not_found(self, url):
		pass

	# api
	def get_random_picture(self):
		pass
