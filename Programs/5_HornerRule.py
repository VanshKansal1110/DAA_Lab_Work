def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result = result * x + arr[i]
    return result

arr=[23,5,2,4]
x=3
print("Result:-", horner(arr,3))