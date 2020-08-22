from wallpaper_parser import WallpaperParser as wp

p = wp(category='fantasy', resolution='1152x864')
print(f'pages: {p.number_of_pages}')
print(f'on one: {p.number_of_pictures_on_page}')
print(f'all: {p.number_of_pictures}')