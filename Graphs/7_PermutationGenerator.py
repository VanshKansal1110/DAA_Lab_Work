import matplotlib.pyplot as plt
import math

perm_count = 0

def permutation(arr, s, e):
    global perm_count
    if s == e:
        perm_count += 1
        return

    for i in range(s, e):
        arr[s], arr[i] = arr[i], arr[s]
        permutation(arr, s + 1, e)
        arr[s], arr[i] = arr[i], arr[s]  # backtrack

n_values = [1, 2, 3, 4, 5, 6,7]

actual = []

for n in n_values:
    perm_count = 0
    arr = list(range(n))
    permutation(arr, 0, n)
    actual.append(perm_count)

assumed = [math.factorial(n) for n in n_values]

plt.plot(n_values, actual, 'o-', label="Actual Permutations")
plt.plot(n_values, assumed, '--', label="O(n!)")

plt.xlabel("n (String Length)")
plt.ylabel("Number of Permutations")
plt.title("Permutation Generator: Actual vs O(n!)")
plt.legend()
plt.grid(True)
plt.show()
