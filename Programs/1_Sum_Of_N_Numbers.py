def sum_n_nums(arr,i):
    if(i==len(arr)):
        return 0
    return arr[i]+ sum_n_nums(arr,i+1)

l=[23,64,24,464,23,876,79]
print(sum_n_nums(l,0))