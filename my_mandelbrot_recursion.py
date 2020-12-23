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


def iterateMandelbrot(initialSet, maxIterations):
    newMandelbrotSet = []
    for c in initialSet:
        x = c ** 2 + c
        if 2 > x.real > -2 and 2 > x.imag > -2:
            newMandelbrotSet.append(x)

    iteration = maxIterations - 1
    print("iteration left", maxIterations, "numbers to process", len(newMandelbrotSet))
    if iteration == 0:
        return newMandelbrotSet
    else:
        return iterateMandelbrot(newMandelbrotSet, iteration)


STEP = 0.001
initial = generateComplexNumberArray(-2, 2, STEP)
mandelbrot = iterateMandelbrot(initial, 200)

plotComplexNumbers(mandelbrot)
