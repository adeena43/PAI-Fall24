l = []
ub = int(input("Enter the length: "))
for i in range(0, ub):
    l.append(int(input("Enter the element: ")))

sum = 0
for i in range(ub):
    sum += l[i]

print("Sum is: ", sum)
