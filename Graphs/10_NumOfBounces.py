import matplotlib.pyplot as plt
import math

call_count = 0

def num_of_bounces(vel):
    global call_count
    call_count += 1
    if vel <= 1:
        return 0
    return 1 + num_of_bounces(vel * 0.425)

velocities = [10, 50, 100, 500, 1000, 5000, 10000]

actual = []

for v in velocities:
    call_count = 0
    num_of_bounces(v)
    actual.append(call_count)

# O(log v)
assumed = [math.log(v) for v in velocities]

plt.plot(velocities, actual, 'o-', label="Actual Recursive Calls")
plt.plot(velocities, assumed, '--', label="O(log v)")

plt.xlabel("Initial Velocity")
plt.ylabel("Number of Calls")
plt.title("Ball Bounces: Actual vs O(log v)")
plt.legend()
plt.grid(True)
plt.show()
