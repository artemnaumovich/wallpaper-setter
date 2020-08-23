from wallpaper_parser import WallpaperParser as wp

p = wp(category='cars', resolution='2560x1600')
print(f'pages: {p.number_of_pages}')
print(f'on one: {p.number_of_pictures_on_page}')
print(f'all: {p.number_of_pictures}')
url='https://wallpaperscraft.com/catalog/cars/2560x1600/page184'
number = 13
page = p.get_picture_page_url_by_number(url, number)
d_u = p.get_picture_download_url(page)
print(d_u)
