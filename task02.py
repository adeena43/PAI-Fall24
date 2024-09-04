try:
    with open(r'file_to_modify.txt') as myFile:
        content = myFile.read()
except Exception as e:
    print(str(e))

toAdd = str(input('Enter the word you want to add: '))
toReplace = str(input('Enter the word you want to remove: '))

replace = content.replace(toReplace,toAdd)

with open('file_to_modify.txt', 'w') as myFile:
    myFile.write(replace)

try:
    with open(r'file_to_modify.txt') as myFile:
        content = myFile.read()
except Exception as e:
    print(str(e))

print(content)