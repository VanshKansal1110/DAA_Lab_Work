import matplotlib.pyplot as plt

def first_duplicate_index(arr):
    ops = 0
    size = len(arr)
    for i in range(size // 2):
        for j in range(i):
            ops += 1
            if arr[j] == arr[i]:
                return ops
    return ops

n_values = [200, 400, 800, 1600, 3200]

actual = []

for n in n_values:
    arr = list(range(n))  # no duplicates → worst case
    actual.append(first_duplicate_index(arr))

assumed = [n * n for n in n_values]  # O(n^2)

# normalize for visibility
scale = actual[-1] / assumed[-1]
assumed = [x * scale for x in assumed]

plt.plot(n_values, actual, 'o-', label="Actual Comparisons")
plt.plot(n_values, assumed, '--', label="O(n²)")

plt.xlabel("n (Array Size)")
plt.ylabel("Comparisons")
plt.title("First Duplicate Index: Actual vs O(n²)")
plt.legend()
plt.grid(True)
plt.show()
