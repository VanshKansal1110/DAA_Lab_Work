def merge(l,s,m,e):
    i = s
    j = m + 1
    temp = []
    while i <= m and j <= e:
        if l[i] <= l[j]:
            temp.append(l[i])
            i += 1
        else:
            temp.append(l[j])
            j += 1
    while i <= m:
        temp.append(l[i])
        i += 1
    while j <= e:
        temp.append(l[j])
        j += 1
    for k in range(len(temp)):
        l[s + k] = temp[k]
    return l

def mergeSort(l,s,e):
    if s >= e:
        return l
    m = s + (e - s) // 2
    mergeSort(l, s, m)
    mergeSort(l, m + 1, e)
    merge(l, s, m, e)
    return l
    
l=list(range(15,0,-1))
print(l)
mergeSort(l,0,len(l)-1)
print(l)