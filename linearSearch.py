from sumOfAnArray import *
array = array('i',[1,2,4,56,788,20])

# use exception
findElement = int(input("Enter a number : "))
for index in range(1, len(array)):
    if array[index] == findElement:
        print("Element index is : ",index)

