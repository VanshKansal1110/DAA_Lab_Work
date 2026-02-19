def min_max(arr, s, e):
    if s == e:
        return arr[s], arr[s]

    if e - s == 1:
        return (arr[s], arr[e]) if arr[s] < arr[e] else (arr[e], arr[s])

    mid = (s + e) // 2
    min1, max1 = min_max(arr, s, mid)
    min2, max2 = min_max(arr, mid + 1, e)

    return min(min1, min2), max(max1, max2)
    
l=[324,5235,23432,5765,678,756345,23123353,6,7867345,457,6587232,5547568,5663443,324345,3450,0,1111111111111]
print(f"list:-{l}\n")
min , max = min_max(l,0,len(l)-1)
print(f"min:-\t{min} \nmax:-\t{max}")