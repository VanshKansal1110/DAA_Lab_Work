import matplotlib.pyplot as plt

step_count = 0

def toh(n):
    global step_count
    if n > 0:
        toh(n - 1)
        step_count += 1
        toh(n - 1)

n_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

actual_steps = []

for n in n_values:
    step_count = 0
    toh(n)
    actual_steps.append(step_count)

# Expected O(2^n)
assumed = [2**n - 1 for n in n_values]

# Plot
plt.plot(n_values, actual_steps, 'o-', label="Actual Moves")
plt.plot(n_values, assumed, '--', label="O(2^n)")

plt.xlabel("Number of Disks (n)")
plt.ylabel("Number of Moves")
plt.title("Tower of Hanoi: Actual vs O(2^n)")
plt.legend()
plt.grid(True)
plt.show()
