def selectItems(l,items,r,c,s):
    if s==len(l):
        return
    if l[s][1]>=c:
        items.append([l[s][0],c,c*r[s]])
    else:
        items.append([l[s][0],l[s][1],l[s][2]])
        selectItems(l,items,r,c-(l[s][1]),s+1)

def Knapsack1(l,c):
    l.sort(key=lambda x: x[2]/x[1], reverse=True)
    ratio=[]
    ratio=[p/w for [a,w,p] in l]
    items=[]
    selectItems(l,items,ratio,c,0)
    return items

def Knapsack2(l,c):
    l.sort(key=lambda x:x[1])
    ratio=[]
    ratio=[p/w for [a,w,p] in l]
    items=[]
    selectItems(l,items,ratio,c,0)
    return items
    
def Knapsack3(l,c):
    l.sort(key=lambda x:x[2], reverse=True)
    ratio=[]
    ratio=[p/w for [a,w,p] in l]
    items=[]
    selectItems(l,items,ratio,c,0)
    return items

l=[('A', 5,30),('C',15,45),('B',10,40),('D',11,77)]
print("Ratio Sorting:-")
capacity=20
items=Knapsack1(l,20)
print("ItemID\t|\tItemWeight\t|\tEarnedProfit\t|")
print("-"*57)
for i in range(len(items)):
    print(items[i][0],"\t|\t",items[i][1],"\t\t|\t",items[i][2], "\t\t|")

totalprofit1=0
for i in range(len(items)):
    totalprofit1+=items[i][2]
print("-"*57,"\n")
    
print("TotalProfit:-\t",totalprofit1)

#--------------------------------------------------------------------------------
items.clear()
items=Knapsack2(l,20)
print("\n\nWeight Sorting:-")
print("ItemID\t|\tItemWeight\t|\tEarnedProfit\t|")
print("-"*57)
for i in range(len(items)):
    print(items[i][0],"\t|\t",items[i][1],"\t\t|\t",items[i][2], "\t\t|")

totalprofit2=0
for i in range(len(items)):
    totalprofit2+=items[i][2]
print("-"*57,"\n")
    
print("TotalProfit:-\t",totalprofit2)

#--------------------------------------------------------------------------------
items.clear()
items=Knapsack3(l,20)
print("\n\nProfit Sorting:-")
print("ItemID\t|\tItemWeight\t|\tEarnedProfit\t|")
print("-"*57)
for i in range(len(items)):
    print(items[i][0],"\t|\t",items[i][1],"\t\t|\t",items[i][2], "\t\t|")

totalprofit3=0
for i in range(len(items)):
    totalprofit3+=items[i][2]
print("-"*57,"\n")
    
print("TotalProfit:-\t",totalprofit3)

#--------------------------------------------------------------------------------

