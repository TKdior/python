"""
print("************Welcome *** To *** my *** Multiplication *** Table *** Generator************")
# Using the for loop
print("Using the for loop to generate a multiplicatin table")
global number
number = int(input("Enter a number to generate its multiplication table:"))
for i in range(0,13):
    print(f"{number} * {i} = {number * i}")
print("Using the while loop to generate a multiplication table")
# using the while loop
i = 0
while i < 13:
    print(f"{number} * {i} = {number * i}")
    i += 1
"""
'''
for i in range(4):
    print(i)
    '''
'''
x = 0
while x<10:
  print(x)
  x +=1
  '''


print("Using the while and the for loops to generate a multiplication table")

  # Using nested loops
for i in range(0, 13):
       number = int(input("Enter a number to generate its multiplication table: "))
       n=0
       while n <13:
           print(f"{n} * {number} = {n * number}")
           n += 1