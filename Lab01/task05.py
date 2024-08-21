l = []
height = int(input("Enter the length of your list: "))

for i in range(height):
    l.append(int(input("Enter the element: ")))

target = int(input("Enter the number: "))


filtered_list = [x for x in l if x > target]

print(filtered_list)
