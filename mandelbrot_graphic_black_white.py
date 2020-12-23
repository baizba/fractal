from PIL import Image, ImageDraw

IMAGE_WIDTH = 600
IMAGE_HEIGHT = 600

REAL_BOTTOM = -2
REAL_TOP = 2
IMAGINARY_BOTTOM = -2
IMAGINARY_TOP = 2

MAX_ITERATION = 80


def mandelbrot(c):
    iteration = 0
    temp_c = 0
    while abs(temp_c) < 2 and iteration < MAX_ITERATION:
        temp_c = temp_c ** 2 + c
        iteration += 1
    return iteration


def get_color_from_iteration(iteration):
    # return 255 - int((MAX_ITERATION / 255 * iteration))
    return 255 - int(iteration * 255 / MAX_ITERATION)


im = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

step_x = abs((REAL_BOTTOM - REAL_TOP)) / IMAGE_WIDTH
step_y = abs((IMAGINARY_BOTTOM - IMAGINARY_TOP)) / IMAGE_HEIGHT
for x in range(IMAGE_WIDTH):
    for y in range(IMAGE_HEIGHT):
        complex_number = complex(x * step_x + REAL_BOTTOM, y * step_y + IMAGINARY_BOTTOM)
        m = mandelbrot(complex_number)
        color = get_color_from_iteration(m)
        draw.point([x, y], (color, color, color))

im.save('output.png', 'PNG')
