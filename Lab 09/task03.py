import matplotlib.pyplot as plt

flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookie Dough", 
           "Rocky Road", "Pistachio", "Mango", "Coffee", "Butter Pecan"]
scoops_sold = [150, 200, 120, 90, 180, 100, 70, 50, 85, 110]

plt.figure(figsize=(8, 8))
plt.pie(scoops_sold, labels=flavors, autopct='%1.1f%%', startangle=140)
plt.title("Ice Cream Sales Distribution by Flavor")
plt.show()
