try:
    a = int(input("Enter an integer value: "))
    b = int(input("Enter another integer value: "))

    print(f"The division of {a} and {b} is {a/b}")

except ZeroDivisionError:
    print("Error: Zero Division Error")

except ValueError:
    print("Plesae enter a valid integer")

except:
    print("Value error: There is some error!")

