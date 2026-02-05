import matplotlib.pyplot as plt

call_count = 0

def truth_table(num, curr_len=0):
    global call_count

    if curr_len == num:
        call_count += 1
        return

    truth_table(num, curr_len + 1)
    truth_table(num, curr_len + 1)

n_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

actual_calls = []

for n in n_values:
    call_count = 0
    truth_table(n)
    actual_calls.append(call_count)

# Expected O(2^n)
assumed = [2**(n) for n in n_values]

# Plot
plt.plot(n_values, actual_calls, 'o-', label="Actual Recursive Calls")
plt.plot(n_values, assumed, '--', label="O(2^n)")

plt.xlabel("Number of Variables (n)")
plt.ylabel("Number of Recursive Calls")
plt.title("Truth Table Generation: Actual vs O(2^n)")
plt.legend()
plt.grid(True)
plt.show()
