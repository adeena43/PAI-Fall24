import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Adina", "Sara", "Hafsa", "Arwa", "Raghib", "Abdul Rahman", "Fahad", "Hamna", "Fatima", "Talha"],
    "Age": [20, 22, 21, 23, 24, 22, 20, 23, 21, 22],
    "Gender": ["Female", "Female", "Female", "Female", "Male", "Male", "Male", "Female", "Female", "Male"]
}

df = pd.DataFrame(data)

gender_counts = df['Gender'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'])
plt.title("Gender Distribution Among Students")
plt.show()
