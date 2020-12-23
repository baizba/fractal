import numpy as np
import matplotlib.pyplot as plt
from typing import List


def generateComplexNumberArray(start, stop, step):
    complexNumbers = []
    for real in np.arange(start, stop, step):
        for imaginary in np.arange(start, stop, step):
            complexNumbers.append(complex(real, imaginary))
    return complexNumbers


def plotComplexNumbers(complexNumbers: List[complex]):
    x = []
    y = []
    for c in complexNumbers:
        x.append(c.real)
        y.append(c.imag)
    plt.plot(x, y, ",")
    plt.show()


STEP = 0.01
mandelbrotSet0 = generateComplexNumberArray(-2, 2, STEP)

# iteration 1
mandelbrotSet1 = []
for c in mandelbrotSet0:
    x = c ** 2 + c
    if 2 > x.real > -2 and 2 > x.imag > -2:
        mandelbrotSet1.append(x)

# iteration 2
mandelbrotSet2 = []
for c in mandelbrotSet1:
    x = c ** 2 + c
    if 2 > x.real > -2 and 2 > x.imag > -2:
        mandelbrotSet2.append(x)

# iteration 3
mandelbrotSet3 = []
for c in mandelbrotSet2:
    x = c ** 2 + c
    if 2 > x.real > -2 and 2 > x.imag > -2:
        mandelbrotSet3.append(x)

# iteration 4
mandelbrotSet4 = []
for c in mandelbrotSet3:
    x = c ** 2 + c
    if 2 > x.real > -2 and 2 > x.imag > -2:
        mandelbrotSet4.append(x)

print(len(mandelbrotSet1), len(mandelbrotSet4))
plotComplexNumbers(mandelbrotSet4)
