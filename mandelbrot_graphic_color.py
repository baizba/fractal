from PIL import Image, ImageDraw, ImageFont

IMAGE_WIDTH = 2000
IMAGE_HEIGHT = 2000

REAL_BOTTOM = -2
REAL_TOP = 0.5
IMAGINARY_BOTTOM = -1.25
IMAGINARY_TOP = 1.25


MAX_ITERATION = 100


def mandelbrot(c):
    iteration = 0
    temp_c = 0
    while abs(temp_c) < 2 and iteration < MAX_ITERATION:
        temp_c = temp_c ** 2 + c
        iteration += 1
    return iteration


def get_color_from_iteration(iteration):
    color_total = int(iteration / MAX_ITERATION * 3 * 255)
    quotient, reminder = divmod(color_total, 255)
    if quotient == 0:
        return 0, 0, reminder
    elif quotient == 1:
        return 0, 255, reminder
    elif quotient == 2:
        return 255, 255, reminder


im = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial")

step_x = (REAL_TOP - REAL_BOTTOM) / IMAGE_WIDTH
step_y = (IMAGINARY_TOP - IMAGINARY_BOTTOM) / IMAGE_HEIGHT
for x in range(IMAGE_WIDTH):
    for y in range(IMAGE_HEIGHT):
        complex_number = complex(x * step_x + REAL_BOTTOM, y * step_y + IMAGINARY_BOTTOM)
        m = mandelbrot(complex_number)
        color = get_color_from_iteration(m)
        draw.point([x, y], color)

# vertical grid bars (100 pixels apart)
for x in range(0, IMAGE_WIDTH, 100):
    draw.line((x, 0, x, IMAGE_HEIGHT), fill=128)
    draw.text((x, IMAGE_HEIGHT / 2 - 10), str(x * step_x + REAL_BOTTOM), fill=(255, 0, 0, 128), font=font)

# horizontal grid bars (100 pixels apart)
for y in range(0, IMAGE_HEIGHT, 100):
    draw.line((0, y, IMAGE_WIDTH, y), fill=128)
    draw.text((IMAGE_WIDTH / 2 + 10, y), str(y * step_y + IMAGINARY_BOTTOM), fill=(255, 0, 0, 128), font=font)

filename = 'output{}x{}.png'.format(IMAGE_WIDTH, IMAGE_HEIGHT)
im.save(filename, 'PNG')
