tableFor = int(input("Enter the number for which you want the multiplication table: "))

i= 1
for i in range(1,11):
    print(f"{tableFor} X {i} = {tableFor*i}")
