l = []
ub = int(input("Enter the length: "))
for i in range(0, ub):
    l.append(int(input("Enter the element: ")))
print(l)
evenCnt = 0
oddCnt = 0
for i in range(ub):
    if (l[i] % 2 == 0):
        evenCnt +=1

    else:
        oddCnt+=1

print("Number of even elements; ",evenCnt)
print("Number of odd elements; ",oddCnt)
