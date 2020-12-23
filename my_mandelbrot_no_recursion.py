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
    newMandelbrot = initialSet
    iteration = maxIterations
    for i in range(0, iteration):
        iteration -= 1
        tempMandelbrot = []
        print("iterations left", iteration, "numbers left", len(newMandelbrot))
        for c in newMandelbrot:
            x = c ** 2 + c
            if abs(x) <= 2:
                tempMandelbrot.append(x)
        newMandelbrot = tempMandelbrot
    return newMandelbrot


STEP = 0.001
START = -1.45
STOP = 1.45
ITERATIONS = 200
initial = generateComplexNumberArray(START, STOP, STEP)
mandelbrot = iterateMandelbrot(initial, ITERATIONS)

plotComplexNumbers(mandelbrot)
