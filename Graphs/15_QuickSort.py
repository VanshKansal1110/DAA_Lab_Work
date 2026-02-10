import time
import math
import matplotlib.pyplot as plt 

def quickSort(l, s, e):
    if s >= e:
        return

    pivot = l[s]
    i = s + 1
    j = e

    while True:
        while i <= e and l[i] <= pivot:
            i += 1
        while l[j] > pivot:
            j -= 1
        if i >= j:
            break
        l[i], l[j] = l[j], l[i]

    l[s], l[j] = l[j], l[s]

    quickSort(l, s, j - 1)
    quickSort(l, j + 1, e)

n_values = [100, 200, 300, 500, 800]
n_values=sorted(n_values)
best_times = []
worst_times = []

for n in n_values:
    # Best Case: already sorted
    best_arr = list(range(n))
    start = time.perf_counter()
    quickSort(best_arr,0,n-1)
    best_times.append(time.perf_counter() - start)

    # Worst Case: reverse sorted
    worst_arr = list(range(n, 0, -1))
    start = time.perf_counter()
    quickSort(worst_arr,0,n-1)
    worst_times.append(time.perf_counter() - start)

# Assumed complexity curves
best_assumed = [n * math.log2(n) for n in n_values]        # O(n.logn)
worst_assumed = [n*n for n in n_values]     # O(n^2)

# Normalize assumed curves
best_scale = best_times[-1] / best_assumed[-1]
worst_scale = worst_times[-1] / worst_assumed[-1]

best_assumed = [x * best_scale for x in best_assumed]
worst_assumed = [x * worst_scale for x in worst_assumed]

# Plot
plt.plot(n_values, best_times, 'o-', label="Actual Best Case")
plt.plot(n_values, best_assumed, '--', label="O(n)")

plt.plot(n_values, worst_times, 'o-', label="Actual Worst Case")
plt.plot(n_values, worst_assumed, '--', label="O(n²)")

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Quick Sort: Best & Worst Case Analysis")
plt.legend()
plt.grid(True)
plt.show()
