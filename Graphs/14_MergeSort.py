import time
import math
import matplotlib.pyplot as plt 

def merge(l,s,m,e):
    i = s
    j = m + 1
    temp = []
    while i <= m and j <= e:
        if l[i] <= l[j]:
            temp.append(l[i])
            i += 1
        else:
            temp.append(l[j])
            j += 1
    while i <= m:
        temp.append(l[i])
        i += 1
    while j <= e:
        temp.append(l[j])
        j += 1
    for k in range(len(temp)):
        l[s + k] = temp[k]

def mergeSort(l,s,e):
    if s >= e:
        return l
    m = s + (e - s) // 2
    mergeSort(l, s, m)
    mergeSort(l, m + 1, e)
    merge(l, s, m, e)

n_values = [1000,100, 300, 500, 1500, 2800, 200, 3000, 3500, 4000, 800, 1600, 3200]
n_values=sorted(n_values)
best_times = []
worst_times = []

for n in n_values:
    # Best Case: already sorted
    best_arr = list(range(n))
    start = time.perf_counter()
    mergeSort(best_arr, 0, n-1)
    best_times.append(time.perf_counter() - start)

    # Worst Case: reverse sorted
    worst_arr = list(range(n, 0, -1))
    start = time.perf_counter()
    mergeSort(worst_arr, 0, n-1)
    worst_times.append(time.perf_counter() - start)

# Assumed complexity curves
assumed = [n * math.log2(n) for n in n_values]        # O(n.logn)

# Normalize assumed curve
best_scale = best_times[-1] / assumed[-1]

assumed = [x * best_scale for x in assumed]

# Plot
plt.plot(n_values, best_times, 'o-', label="Actual Best Case")
plt.plot(n_values, assumed, '--', label="O(n.logn)")

plt.plot(n_values, worst_times, 'o-', label="Actual Worst Case")

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Merge Sort: Best & Worst Case Analysis")
plt.legend()
plt.grid(True)
plt.show()