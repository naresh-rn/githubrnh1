"""
Find Last Digit Of a^b for Large Numbers
input a = 9 , b = 5
output as 9*9*9*9*9 = 59049
last digit is : 9
"""
number_one, number_two = int(input("Enter first operand : ")), int(input("Enter the power operand : "))
result = number_one ** number_two                # Exponentiation operator
print("Last digit is : ", int(str(result)[-1]))  # type casting for access the lastDigit with index
