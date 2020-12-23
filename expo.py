import matplotlib.pyplot as plt

exponents = []
results = []
total = 0
for exponent in range(0, 64):
    currentIterationResult = 2 ** exponent
    exponents.append(exponent)
    results.append(currentIterationResult)
    total += currentIterationResult
    print("2**{} = {}".format(exponent, currentIterationResult))
print("sum of all iterations:", total)
plt.plot(exponents, results)
plt.show()
