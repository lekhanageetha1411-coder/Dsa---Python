#accounts = [[1,2,3],[2,3,4]]

max_wealth = 0

for customer in account:
    total = sum(customer)
    if total >max_wealth:
        max_wealth = total 

print(max_wealth)

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

#accounts = [[1,2,3],[2,3,4]]

cus = int(input("ENter the number of customer:"))

account = []

for i in range(cus):
    amounts = input("amount of each cus:"+str(i+1)+":")
    number = list(map(int,amounts.split()))
    account.append(number)

max_wealth = 0

for customer in account:
    total = sum(customer)
    if total >max_wealth:
        max_wealth = total 

print(max_wealth)