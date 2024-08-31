
temperatures = [
    32, 35, 30, 31, 33, 34, 36, 33, 31, 32, 35, 37, 
    38, 36, 35, 34, 33, 32, 31, 30, 29, 28, 30, 31, 
    32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 41, 40, 
    39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28
]

min_temp = temperatures[0]
max_temp = temperatures[0]

for temp in temperatures:
    if temp < min_temp:
        min_temp = temp
    if temp > max_temp:
        max_temp = temp

sorted_temperatures = temperatures[:]
n = len(sorted_temperatures)

for i in range(n):
    for j in range(0, n-i-1):
        if sorted_temperatures[j] > sorted_temperatures[j+1]:
            # Swap if the element found is greater than the next element
            sorted_temperatures[j], sorted_temperatures[j+1] = sorted_temperatures[j+1], sorted_temperatures[j]

print(f"Minimum temperature: {min_temp}")
print(f"Maximum temperature: {max_temp}")
print(f"Sorted temperatures: {sorted_temperatures}")
