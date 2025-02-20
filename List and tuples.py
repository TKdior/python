"""
digits = list(range(50))
digits
even_digits = [number for number in range(1,10) if number % 2 == 0]
even_digits
anything = [1,2,"moi","thanks"]
"""
'''
args_tuple = (5,7,5,8,1)
def number_args(*number):
  print (number[0] * number[1] )
number_args(*args_tuple)
'''

def number_squared(number,power):
    print(number**power)
    number_squared (power=4, number=10)
number_squared(10,4)