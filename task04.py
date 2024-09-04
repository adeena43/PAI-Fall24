user_name = str(input('Enter your name: '))
user_cnic = int(input('Enter your cnic number: '))
user_age = int(input('Enter your age: '))
user_sal = int(input('Enter your salary: '))

list1 = [user_name,user_cnic,user_age,user_sal]
try:
    with open('text.txt','a') as myFile:
        for i in range(len(list1)):
            myFile.write(str(f"{list1[i]}\n"))
except Exception as e:
    print(str(e))

number = int(input('Enter your contact number: '))

try:
    with open('info.txt','a') as myFile:
        myFile.write(str(number))
except Exception as e:
    print(str(e))