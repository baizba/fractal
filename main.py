import matplotlib.pyplot as plt

iterations = []
results = []
x = 1
for i in range(1, 10):
    iterations.append(x)
    x = x**2 + 1
    results.append(x)
print(iterations)
print(results)
plt.plot(iterations, results)
plt.show()
