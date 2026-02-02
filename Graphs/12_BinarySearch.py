import matplotlib.pyplot as plt
import math

call_count = 0

def binary_search(arr, key, s, e):
    global call_count
    call_count += 1

    if s > e:
        return -1

    m = (s + e) // 2
    if arr[m] == key:
        return m
    elif arr[m] > key:
        return binary_search(arr, key, s, m - 1)
    else:
        return binary_search(arr, key, m + 1, e)

n_values = [10, 50, 100, 500, 1000, 5000, 10000]

actual = []

for n in n_values:
    arr = list(range(n))
    call_count = 0
    binary_search(arr, -1, 0, n - 1)  # worst case (not found)
    actual.append(call_count)

assumed = [math.log2(n) for n in n_values]

plt.plot(n_values, actual, 'o-', label="Actual Calls")
plt.plot(n_values, assumed, '--', label="O(log n)")

plt.xlabel("n (Array Size)")
plt.ylabel("Recursive Calls")
plt.title("Binary Search: Actual vs O(log n)")
plt.legend()
plt.grid(True)
plt.show()
