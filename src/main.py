
from general_parser import GeneralParser
from wallpaper_parser import WallpaperParser
from time import time
import ctypes
import eel



eel.init('web')


@eel.expose
def ping(x):
	print(f'message: {x}')
	return 'pong'


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


def read_data():
	directory = input('Input directory: ').strip()
	category = input('Input category: ').strip()
	resolution = input('Input resolution: ').strip()
	return directory, category, resolution


@eel.expose
def build_path(directory, category, resolution):
	file_path = f'{directory}/{category}_{resolution}_{int(time())}.jpg'
	return file_path

eel.start('index.html', size=(900, 600))


'''
def main():	
 	directory, category, resolution = read_data()
	path = build_path(directory=directory, category=category, resolution=resolution)
	url = get_picture_url(category=category, resolution=resolution)
	save_picture(path=path, url=url)
	set_wallpaper(path)
if __name__ == '__main__':
	main()
'''