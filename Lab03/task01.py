try:
    with open("helloWorld.txt", "r") as myFile:
        count = 0
        word = 0

        for i in myFile:
            word+= len(i.split())
            count = len(i)

        print(f"Word count: {word}")
        print(f"Character count: {count}")

except IOError:
    print("IDnput/Output error ocurred")

except FileNotFoundError:
    print("File not found")
