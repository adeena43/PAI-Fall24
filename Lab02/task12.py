
list1 = input("Enter the elements of the first list separated by spaces: ").split()
list2 = input("Enter the elements of the second list separated by spaces: ").split()
if len(list1) != len(list2):
    print("Error: The lists must have the same number of elements.")
else:
    dictionary = {}
    for i in range(len(list1)):
        key = list1[i]
        value = list2[i]
        dictionary[key] = value
    print("Resulting dictionary:")
    print(dictionary)
