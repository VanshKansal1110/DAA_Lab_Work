import time
import matplotlib.pyplot as plt

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

n_values = [500, 1000, 2000, 4000, 8000]
actual_times = []

for n in n_values:
    arr = list(range(n))
    key = -1  # worst case: not present

    start = time.perf_counter()
    linear_search(arr, key)
    actual_times.append(time.perf_counter() - start)

# Expected O(n)
assumed = [n for n in n_values]

# Normalize
scale = actual_times[-1] / assumed[-1]
assumed = [x * scale for x in assumed]

# Plot
plt.plot(n_values, actual_times, 'o-', label="Actual Time")
plt.plot(n_values, assumed, '--', label="O(n)")

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Linear Search: Actual vs O(n)")
plt.legend()
plt.grid(True)
plt.show()
