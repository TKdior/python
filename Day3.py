print("************Welcome *** to *** my *** Guessing *** Number *** game************")
# Dictionary of numbers and their index
Dictionary_numbers = {
   0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10
}

# Assigning an index to the target number
target_number = Dictionary_numbers[4]

# Enter the guess number ensuring it's an integer
print("Ensure your number isn't above 10 and less than 0 ")
number = int(input("Enter a number:"))

# The Conditions
if number <0 or number > 10:
    print("Enter a number between 0 and 10!")
elif number == target_number:
    print("Perfect Match!")
elif number < target_number:
    print("The number is lower than the target")
elif number > target_number:
    print("Too big to be the target")


