import matplotlib.pyplot as plt
import time

def min_max(arr, s, e):
    if s == e:
        return arr[s], arr[s]

    if e - s == 1:
        return (arr[s], arr[e]) if arr[s] < arr[e] else (arr[e], arr[s])

    mid = (s + e) // 2
    min1, max1 = min_max(arr, s, mid)
    min2, max2 = min_max(arr, mid + 1, e)

    return min(min1, min2), max(max1, max2)
    
n_sizes=[200,500,1000,1400,1800,2000,2400,2900,3500,4000]
n_sizes= sorted(n_sizes)

time_taken=[]

for i in n_sizes:
    arr=list(range(i))
    t= time.perf_counter()
    min_max(arr,0,len(arr)-1)
    time_taken.append(time.perf_counter()-t)
    
assumed=n_sizes.copy()
scale= time_taken[-1]/assumed[-1]

assumed=[x*scale for x in assumed]

plt.plot(n_sizes, time_taken, 'o-', label="Actual Best Case")
plt.plot(n_sizes, assumed, '--', label="O(n")

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Min–Max using Divide & Conquer")
plt.legend()
plt.grid(True)
plt.show()