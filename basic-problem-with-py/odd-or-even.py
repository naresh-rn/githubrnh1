check_odd_even = lambda number: "Even" if number % 2 == 0 else "Odd"

num = int(input("Enter a number: "))
result = check_odd_even(num)
print("The number is", result)
