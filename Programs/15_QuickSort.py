import random

def quickSort(l,s,e):
    if(s>e):
        return l
    v=l[s]
    i=s 
    j=e
    while i<=j:
        while i<len(l) and l[i]<=v:
            i+=1
        while j>=0 and l[j]>v:
            j-=1
        if i<j:
            l[i],l[j]=l[j], l[i]
    l[s]=l[j]
    l[j]=v
    quickSort(l,s,j-1)
    if(j<len(l)-1):
        quickSort(l,j+1,e)

size=20

l=[]
for i in range(size):
    l.append(random.randint(1,100))
print(l)
quickSort(l,0, len(l)-1)
print(l)