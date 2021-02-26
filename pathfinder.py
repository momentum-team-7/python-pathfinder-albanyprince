from PIL import Image, ImageColor, ImageDraw
# import math

# read file and store it as a list of lists

# def small_map_elev():
#     with open("elevation_small.txt", 'r') as small_elev_file:
#         small_map = small_elev_file.readlines()
#         print("read lines", small_map)
coordinates = []   
with open('elevation_small.txt', 'r') as file:
    for coord_line in file.readlines():
        coordinates.append(coord_line.split())
    # print(coordinates)    

max_el = int(max(map(max, coordinates)))
print(max_el)
min_el = int(min(map(min, coordinates)))
print(min_el)

el_delta = int((max_el) - (min_el))
print (el_delta)



# image dimensions 
# rows = len(coordinates)
# columns = len(coordinates[0])
dimensions = len(coordinates), len(coordinates[0])
# def get_color(elevation, min, max):
print(dimensions)

def get_color_value(elevation, min_el, max_el): 
    color_value = (int(elevation) - min_el) / el_delta * 255
    # color_value = (((int(elevation) - min_el)/(el_delta)) * 255)
    return(int(color_value), int(color_value), int(color_value))

im = Image.new('RGB', (dimensions))
    # im.save('elevation_small.png')
    # Image.open('elevation_small.png')
    # im.getpixel((0,0))
for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        # breakpoint()        
        im.putpixel((x,y), get_color_value(coordinates[y][x], min_el, max_el))
        # for every x and y, it must be grouped together in a tuple
        # y = list number x = item within the list
       
im.save('elevation_small.png')   
# draw line
def draw_path(coordinates):
    im = Image.open('elevation_small.png')
    draw = ImageDraw.Draw(im)
    line_color = (50, 205, 50)
    draw.line((y1,x1, y2,x2), fill=line_color, width = 10)
#     # draw.line((y, im.size[1], im.size[0], x), fill=128)
    

im.save('path.png')    

