size = int(input("Enter size of the list: "))
my_list = [int(input(f"Enter {i+1} value: ")) for i in range(size)]
r_list = []

for i in range(len(my_list)-1,-1,-1):
    r_list.append(my_list[i])

print(f"Original List: {my_list}")
print(f"Reversed List: {r_list}")
