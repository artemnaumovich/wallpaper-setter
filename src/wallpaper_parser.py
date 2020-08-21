# wallpaper parser

import requests
import settings
from bs4 import BeautifulSoup as bs




def get_html(url, params):
	pass


def get_resolution_page_url(resolution):# build
	pass


def get_first_page_url(resolution, category):# build
	pass


def get_number_of_pages(resolution, category):# parse
	pass


def get_page_url_by_number(resolution, category, number):# build
	pass


def get_last_page_url(resolution, category):# build
	pass


def get_number_of_pictures_on_page(url):# parse
	pass


def get_number_of_pictures(category, resolution):# parse public
	pass


def get_page_content_by_number(resolution, category, number):# parse
	pass


def get_picture_on_page_by_number(url, number):# parse
	pass


def get_picture_page_download_url(url):# parse
	pass


def get_picture_by_number(resolution, category, number):# parse public
	pass
	