
from general_parser import GeneralParser
from wallpaper_parser import WallpaperParser
from exceptions import NoSuchResolutionException
from time import time
import ctypes
import eel


@eel.expose
def get_filters():
	return WallpaperParser.get_filters()


@eel.expose
def get_picture_url(category, resolution):
	parser = WallpaperParser(category=category, resolution=resolution)
	picture_url = parser.get_random_picture_url()
	return picture_url


@eel.expose
def save_picture(path, url):
	parser = GeneralParser()
	picture = parser.download_picture(url)
	with open(path, 'wb') as f:
		f.write(picture)


@eel.expose
def set_wallpaper(path):	
	SPI_SETDESKWALLPAPER    = 0x0014
	SPI_SETDESKPATTERN      = 0x0015
	SPIF_UPDATEINIFILE      = 0x01
	SPIF_SENDWININICHANGE   = 0x02
	ctypes.windll.user32.SystemParametersInfoW(
		SPI_SETDESKWALLPAPER,
		0,
		path,
		SPIF_SENDWININICHANGE | SPIF_UPDATEINIFILE
	)


@eel.expose
def set_picture(path, url, category, resolution):
	picture_path = build_path(path, category, resolution)
	save_picture(picture_path, url)
	set_wallpaper(picture_path)


def read_data():
	directory = input('Input directory: ').strip()
	category = input('Input category: ').strip()
	resolution = input('Input resolution: ').strip()
	return directory, category, resolution


# @eel.expose
# def is_path_exists(path):
# 	pass


# need to refactor(join path)
@eel.expose
def build_path(directory, category, resolution):
	file_path = f'{directory}/{category}_{resolution}_{int(time())}.jpg'
	return file_path


def main():	
	eel.init('web')
	eel.start('index.html', size=(900, 600))


if __name__ == '__main__':
	main()
