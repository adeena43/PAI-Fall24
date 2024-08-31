l = [34, 67, 42, 23, 50]

total_sum = 0
for i in l:
    total_sum += i

avg = total_sum / len(l)
print(f"Average: {avg}")

max_val = l[0]  
for i in l:
    if i > max_val:
        max_val = i

print(f"Maximum is: {max_val}")

min_val = l[0]  
for i in l:
    if i < min_val:
        min_val = i

print(f"Minimum is: {min_val}")

l.sort()  # This sorts the list in place
print(f"Sorted list: {l}")
removed_element = l.pop(2)  
print(f"Removed third element from the list: {removed_element}")
