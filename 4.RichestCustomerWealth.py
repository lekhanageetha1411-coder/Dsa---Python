class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0

        for customer in accounts:
            total = sum(customer)

            if total > max_wealth:
                max_wealth = total

        return max_wealth


or 
accounts = [[1,2,3],[2,3,4]]

max_wealth = 0

for customer in accounts:
    total = sum(customer)
    if total >max_wealth:
        max_wealth = total 


or 

num_customers = int(input("Enter number of customers: "))

accounts = []

for i in range(num_customers):

    amounts = input("Enter amounts for customer " + str(i+1) + ": ") #i starts from 0 But customers start from 1

    numbers = list(map(int, amounts.split())) #amounts = "1 2 3"  Take input string
→ split into pieces
→ convert to integers
→ store in list
  #amounts.split()  ["1", "2", "3"]
  #map(int, ["1", "2", "3"])
  #res = 1, 2, 3
  

    accounts.append(numbers)

max_wealth = 0

for customer in accounts:

    total = sum(customer)

    if total > max_wealth:
        max_wealth = total

print("Richest customer wealth is:", max_wealth)
print(max_wealth)
