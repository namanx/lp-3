n = int(input("Enter the number of items: "))
maxwt = int(input("Maximum weight: "))
profit = list(map(int, input("Enter profit value of items: ").split()))
weight = list(map(int, input("Enter weight of items: ").split()))

wt = 0
max_profit = 0

ppw = []
for i in range(n):
    ppw.append(profit[i] / weight[i])

order = []  
for i in range(n):
    order.append(ppw.index(max(ppw)))
    ppw[ppw.index(max(ppw))] = 0

i = 0

print("\nItems in Knapsack:")
print("Item\tWeight\tProfit Value\tFraction")

while wt != maxwt and i < n:
    if (wt + weight[order[i]]) <= maxwt:
        max_profit += profit[order[i]]
        wt += weight[order[i]]
        print("%d\t\t%d\t\t%d\t\t\t\t1" % (order[i] + 1, weight[order[i]], profit[order[i]]))
    else:
        fraction = (maxwt - wt) / weight[order[i]]
        value = profit[order[i]] * fraction
        max_profit += value
        wt = maxwt
        print("%d\t\t%d\t\t%0.2f\t\t\t\t%0.2f" % (order[i] + 1, weight[order[i]], value, fraction))
    i += 1

print("\nMaximum profit = %0.2f" % max_profit)

"""
Enter the number of items: 5
Maximum weight: 10 
Enter profit value of items: 10 15 10 12 8
Enter weight of items: 3 3 2 5 1

Items in Knapsack:
Item    Weight  Profit Value    Fraction
5               1               8                               1
2               3               15                              1
3               2               10                              1
1               3               10                              1
4               5               2.40                            0.20

Maximum profit = 45.40
"""