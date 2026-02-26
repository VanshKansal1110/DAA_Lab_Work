import time
import matplotlib.pyplot as plt
import random

def sum_n_nums(arr):
    total = 0
    for x in arr:
        total += x
    return total

n_values = [100, 200,500, 800, 1000, 2000, 2200, 2500,3000, 3500, 4000]
n_values=sorted(n_values)
actual_times = []

for n in n_values:
    arr = [random.randint(1, 100) for _ in range(n)]
    start = time.perf_counter()
    sum_n_nums(arr)
    actual_times.append(time.perf_counter() - start)

# Assumed O(n)
assumed = [n for n in n_values]

# Normalize
scale = actual_times[-1] / assumed[-1]
assumed = [x * scale for x in assumed]

# Plot
plt.plot(n_values, actual_times, 'o-', label="Actual Time")
plt.plot(n_values, assumed, '--', label="O(n)")

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sum of n Numbers: Actual vs O(n)")
plt.legend()
plt.grid(True)
plt.show()
