length = int(input('Enter the length of lists: '))
list_1 = []
list_2 = []
dicts = {}

print('Enter elements for list 1: ')
for i in range(length):
    list_1.append(int(input('Enter the element: ')))

print('Enter elements for list 2: ')
for i in range(length):
    list_2.append(input('Enter the element: '))

for i in range(len(list_1)):
    dicts[list_1[i]] = list_2[i]

try:
    with open('task_3.txt', 'w') as myFile:
       myFile.write(str(dicts))
except Exception as e:
    print(str(e))