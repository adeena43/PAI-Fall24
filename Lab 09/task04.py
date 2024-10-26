import matplotlib.pyplot as plt

ages = [20, 22, 25, 28, 29, 32, 34, 36, 38, 21, 24, 27, 31, 35, 23, 29, 26, 33, 37, 39, 22, 30]

age_groups = {"18-25": 0, "26-30": 0, "31-35": 0, "36 and above": 0}
for age in ages:
    if 18 <= age <= 25:
        age_groups["18-25"] += 1
    elif 26 <= age <= 30:
        age_groups["26-30"] += 1
    elif 31 <= age <= 35:
        age_groups["31-35"] += 1
    else:
        age_groups["36 and above"] += 1

labels = age_groups.keys()
sizes = age_groups.values()

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Student Age Distribution by Age Group")
plt.show()
