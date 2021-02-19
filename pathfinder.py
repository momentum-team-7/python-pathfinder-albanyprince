
# read file and store it as a list of lists

# def small_map_elev():
#     with open("elevation_small.txt", 'r') as small_elev_file:
#         small_map = small_elev_file.readlines()
#         print("read lines", small_map)
coordinates = []   
with open('elevation_small.txt', 'r') as file:
    for coord_line in file.readlines():
        coordinates.append(coord_line.split())
    print(coordinates)    

max_el = int(max(map(max, coordinates)))
print(max_el)
min_el = int(min(map(min, coordinates)))
print(min_el)

el_delta = int((max_el) - (min_el))
print (el_delta)
       
# def get_color(elevation, min, max):
from PIL import Image, ImageColor

im = Image.new('RGB', (600, 600))
im.save('elevation_small.png')
# Image.open('elevation_small.png')
im.getpixel((0,0))
for x in range(600):
    for y in range(600):
        im.putpixel((x,y), (150,150,150))
    # find elevation and find grayscale for that elevation that will get passed into line 31
im.save('putpixel.png')    
 
def color_value = ((elevation - min_elevation)/(max_el - min_el)) * 255
# tuple
    color_value = (((int(elevation) - min_el)/(el_delta)) * 255)
    print(int(color_value), int(color_value), int(color_value))