import matplotlib.pyplot as plt

def missing_num(arr):
    ops = 0
    size = len(arr)

    i = 0
    while i < size:
        ops += 1
        if arr[i] == size:
            i += 1
            continue
        if arr[i] != i:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
            ops += 1
        else:
            i += 1
    return ops

n_values = [100, 500, 1000, 2000, 4000, 8000]

actual = []

for n in n_values:
    arr = list(range(n + 1))
    arr.pop(n // 2)          # remove one element
    actual.append(missing_num(arr))

assumed = n_values  # O(n)

plt.plot(n_values, actual, 'o-', label="Actual Operations")
plt.plot(n_values, assumed, '--', label="O(n)")

plt.xlabel("n (Array Size)")
plt.ylabel("Operation Count")
plt.title("Missing Number Algorithm: Actual vs O(n)")
plt.legend()
plt.grid(True)
plt.show()
