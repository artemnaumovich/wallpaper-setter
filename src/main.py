
from wallpaper_parser import WallpaperParser
from time import time
import ctypes


def get_picture(category, resolution):
	parser = WallpaperParser(category=category, resolution=resolution)
	picture = parser.get_random_picture()
	return picture


def save_picture(path, picture):
	with open(path, 'wb') as f:
		f.write(picture)


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


def build_path(directory, category, resolution):
	file_path = f'{directory}/{category}_{resolution}_{int(time())}.jpg'
	return file_path


def main():
	
	directory, category, resolution = read_data()
	path = build_path(directory=directory, category=category, resolution=resolution)

	picture = get_picture(category=category, resolution=resolution)
	save_picture(path=path, picture=picture)
	set_wallpaper(path)


if __name__ == '__main__':
	main()
