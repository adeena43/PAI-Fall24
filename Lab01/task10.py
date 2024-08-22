l = []
length = int(input("Enter the length of your list: "))

for i in range(length):
    l.append(int(input("Enter the element: ")))

max_value = l[0]

for num in l:
    if num > max_value:
        max_value = num

print(f"The maximum value is: {max_value}")
