import matplotlib.pyplot as plt

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
    totalprofit=0
    for i in range(len(items)):
        totalprofit+=items[i][2]

    return totalprofit

def Knapsack2(l,c):
    l.sort(key=lambda x:x[1])
    ratio=[]
    ratio=[p/w for [a,w,p] in l]
    items=[]
    selectItems(l,items,ratio,c,0)
    totalprofit=0
    for i in range(len(items)):
        totalprofit+=items[i][2]

    return totalprofit
    
def Knapsack3(l,c):
    l.sort(key=lambda x:x[2], reverse=True)
    ratio=[]
    ratio=[p/w for [a,w,p] in l]
    items=[]
    selectItems(l,items,ratio,c,0)
    totalprofit=0
    for i in range(len(items)):
        totalprofit+=items[i][2]

    return totalprofit

items = [
    ('A', 5, 30),
    ('B', 10, 40),
    ('C', 15, 45),
    ('D', 11, 77),
    ('E', 7, 35),
    ('F', 9, 50)
]

capacities = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

result_1=list()
result_2=list()
result_3=list()

for i in capacities:
    profit1=Knapsack1(items,i)
    profit2=Knapsack2(items,i)
    profit3=Knapsack3(items,i)
    result_1.append(profit1)
    result_2.append(profit2)
    result_3.append(profit3)
    
plt.plot(capacities,result_1,'o-',label="Ratio-Based")
plt.plot(capacities,result_2,'o-',label="Weight-Based")
plt.plot(capacities,result_3,'o-',label="Profit-Based")

plt.xlabel("Capacities")
plt.ylabel("Total_Profit_Earned")
plt.title("Comparison of Greedy Knapsack Strategies")
plt.legend()
plt.grid(True)
plt.show()