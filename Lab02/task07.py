l = [34, 67, 42, 23, 50]
sum = 0
max = 0
min = 0
for i in l:
    sum = sum+i

avg = sum/len(l)
print(f"Average: {avg}")
for i in l:
    if i>max: 
        max = i 

print(f"Maximum is: {max}")

for i in l:
    if i<min: 
        min = i 

print(f"Minimum is: {min}")

l = l.sort()
print(f"Sorted list: {l}")

l = l.pop(2)
print(f"Removed third element from the lis: {l}")
