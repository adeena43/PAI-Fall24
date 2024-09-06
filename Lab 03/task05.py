import json

try:
    my_dict = {}
    num_entries = int(input("Enter the number of pairs you want to enter: "))
    for _ in range(num_entries):
        key = input("Enter the name: ").strip()
        value = int(input("Enter the age of the person: "))
        my_dict[key] = value
    with open("Q_5.json", "w") as myFile:
        json.dump(my_dict, myFile)
    with open("Q_5.json", "r") as myFile:
        data = json.load(myFile)
    max_age = max(data.values())
    name_with_max_age = [name for name, age in data.items() if age == max_age]
    print(f"The person(s) with maximum age ({max_age}) is/are: {', '.join(name_with_max_age)}")
    ages = list(data.values())
    seen_ages = set()
    duplicate_ages = set()

    for age in ages:
        if age in seen_ages:
            duplicate_ages.add(age)
        else:
            seen_ages.add(age)

    if duplicate_ages:
        print(f"Ages that are shared among people: {', '.join(map(str, duplicate_ages))}")
    else:
        print("No one shares the same age.")

except json.JSONDecodeError as e:
    print(f"Error reading JSON data: {e}")
except IOError as e:
    print(f"An IOError occurred: {e}")
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
