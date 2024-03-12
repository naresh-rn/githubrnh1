from array import *

def sumOfArray(array_list):                         # function definition
    sum = 0
    for item in range(0, len(array_list)):
        sum = sum + array_list[item]
    return sum
# function calling
array_list = array('i', [54,47,68,84,927,10])
print("Sum of array is :",sumOfArray(array_list))