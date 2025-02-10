""" 
# Hello, World!
 Hello my name is Zaina 
I’m an intern in TIC(Tech Innovation Center)
This is my second day report on Python

# Variables Declarations
a = 5
print(a)
name = "Zaina" 
print(name)
# Swapping two variables 
a,b = 1,2
print ("a = ", b, "b = ",a)

# Data types 
n = "8"
x = int(n)
print(x)
print(type(n))
print(type(x))

s = 6
e = float(s)
print(s)
print(type(s))
print(type(e))

num = 10
print(num)
r = str(num)
print(type(num))
print(type(r))

# Using the del for deletion 
r= 8
print(x)

del r
# counting characters in a string 
word = "Romaric" 
length = len(word)
print("Length of the word is",length)

#local variables 
def f():
    q = "I'm a girl "
    f()

    # global variable
    k = 74
    def f():
        global k
        k = 79
        print(k)
        f()
        print(k)
"""


        # program that input and displays age in days
age = int(input("Enter your age:"))
print(age)

age_days = age * 365
print("Your age in days is ",age_days,"days")