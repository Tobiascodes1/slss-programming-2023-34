from PIL import Image

import colour_helper

red_ball_image = Image.open("./Images/Red Ball.jpeg")

RED_PIXEL = (150, 0, 0)

red_pixels = []

for y in range(red_ball_image.height):
    for x in range(red_ball_image.width):
        current_pixel = red_ball_image.getpixel((x, y))

        if colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))

x_coords = [coord[0] for coord in red_pixels]
y_coords = [coord[1] for coord in red_pixels]
sx = min(x_coords)
mx = max(x_coords)
sy = min(y_coords)
my = max(y_coords)
pupx = (sx + mx)/2
pupy = (sy + my)/2

robo_pup = (pupx,pupy)
print(robo_pup)

original_size = (red_ball_image.width, red_ball_image.height)
red_pixel_map = Image.new("RGB", original_size)

for pixel_loc in red_pixels:
    red_pixel_map.putpixel(pixel_loc, RED_PIXEL)

red_pixel_map.save("./Images/red_pixel_map.jpg")


red_pixel_map.close()
red_ball_image.close()
