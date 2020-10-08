
from general_parser import GeneralParser
from wallpaper_parser import WallpaperParser
from exceptions import OSIsNotSupportedError
from time import time
import ctypes
import eel
import constants
import os


@eel.expose
def get_filters():
	return WallpaperParser.get_filters()


@eel.expose
def get_picture_url(category, resolution, cache={}):
	key = (category, resolution)
	if key in cache and time() - cache[key]['time_stamp'] <= constants.RELOAD_TIME:
		parser = cache[key]['parser']
	else:
		parser = WallpaperParser(category=category, resolution=resolution)
		upd = {
			'parser': parser,
			'time_stamp': time()
		}
		cache[key] = upd
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
	if path == '' or not os.access(path, os.F_OK):
		raise FileNotFoundError
	picture_path = build_path(path, category, resolution)
	save_picture(picture_path, url)
	set_wallpaper(picture_path)


def read_data():
	directory = input('Input directory: ').strip()
	category = input('Input category: ').strip()
	resolution = input('Input resolution: ').strip()
	return directory, category, resolution


@eel.expose
def build_path(directory, category, resolution):
	file_name = f'{category}_{resolution}_{int(time())}.jpg'
	abs_path = os.path.join(directory, file_name)
	return abs_path


def main():	
	eel.init('web')
	eel.start('index.html', size=(constants.WIDTH, constants.HEIGHT))


if __name__ == '__main__':
	main()
