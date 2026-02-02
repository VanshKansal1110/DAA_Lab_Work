import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    if(len(arr)>1):
        for i in range[1,len(arr)]:
            if  arr[0]>arr[i]:
                arr[0],arr[1]=arr[1], arr[0]
    selection_sort(arr[1:])

n_values = [1000, 4000, 800, 1600, 3200]
n_values=sorted(n_values)
best_times = []
worst_times = []

for n in n_values:
    # Best Case: already sorted
    best_arr = list(range(n))
    start = time.perf_counter()
    selection_sort(best_arr)
    best_times.append(time.perf_counter() - start)

    # Worst Case: reverse sorted
    worst_arr = list(range(n, 0, -1))
    start = time.perf_counter()
    selection_sort(worst_arr)
    worst_times.append(time.perf_counter() - start)

# Assumed complexity curves
best_assumed = [n for n in n_values]        # O(n)
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
plt.title("Insertion Sort: Best & Worst Case Analysis")
plt.legend()
plt.grid(True)
plt.show()
