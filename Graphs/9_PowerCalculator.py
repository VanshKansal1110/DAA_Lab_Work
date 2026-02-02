import matplotlib.pyplot as plt
import math

call_count = 0

def power(num, pow):
    global call_count
    call_count += 1

    if pow == 0:
        return 1
    if pow == 1:
        return num
    if pow > 1:
        if pow % 2 == 0:
            return power(num * num, pow // 2)
        else:
            return num * power(num * num, (pow - 1) // 2)
    else:
        return 1 / power(num, -pow)

pow_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

actual = []

for p in pow_values:
    call_count = 0
    power(2, p)
    actual.append(call_count)

assumed = [math.log2(p) for p in pow_values]

plt.plot(pow_values, actual, 'o-', label="Actual Recursive Calls")
plt.plot(pow_values, assumed, '--', label="O(log n)")

plt.xlabel("Exponent (n)")
plt.ylabel("Recursive Calls")
plt.title("Fast Power Algorithm: Actual vs O(log n)")
plt.legend()
plt.grid(True)
plt.show()
