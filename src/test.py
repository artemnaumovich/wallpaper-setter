from wallpaper_parser import WallpaperParser as wp


p = wp(category='textures', resolution='1920x1080')
print(f'pages: {p.number_of_pages}')
print(f'on one: {p.number_of_pictures_on_page}')
print(type(p.get_random_picture()))

