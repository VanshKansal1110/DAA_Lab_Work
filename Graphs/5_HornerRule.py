import time
import matplotlib.pyplot as plt
import random

def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result = result * x + arr[i]
    return result

n_values = [500, 1000, 2000, 4000, 8000]
actual_times = []

for n in n_values:
    coeffs = [random.randint(1, 10) for _ in range(n)]
    x = 2

    start = time.perf_counter()
    horner(coeffs, x)
    actual_times.append(time.perf_counter() - start)

# Expected O(n)
assumed = [n for n in n_values]

# Normalize
scale = actual_times[-1] / assumed[-1]
assumed = [x * scale for x in assumed]

# Plot
plt.plot(n_values, actual_times, 'o-', label="Actual Time")
plt.plot(n_values, assumed, '--', label="O(n)")

plt.xlabel("Polynomial Degree (n)")
plt.ylabel("Time (seconds)")
plt.title("Horner's Rule: Actual vs O(n)")
plt.legend()
plt.grid(True)
plt.show()
