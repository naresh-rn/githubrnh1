from array import *
# Function for Find Minimum value in Array
def minimumElement(array):
  minimum = array[0]
  for item in range(0, len(array)):
    if array[item] < minimum:
      minimum = array[item]
  return minimum
# Function to find Maximum value in Array  
def maximumElement(array):
  maximum = array[0]
  for item in range(0, len(array)):
    if array[item] > maximum:
      maximum = array[item]
  return maximum

array = array('i', [267,289,128,190,2199])

print(f"Minimum Value is : {minimumElement(array)}.\nMaximum Value is : {maximumElement(array)}.")
# or
"""
maximum_value = maximumElement(array)
minimum_value = minimumElement(array)
print("Minimum value is : ", minimum_value,"maximum value is : ",maximum_value )
"""