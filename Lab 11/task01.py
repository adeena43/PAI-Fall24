# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the dataset
file_path = "heart.csv"  
heart_data = pd.read_csv(file_path)

# Separate features (X) and target (y)
X = heart_data.drop(columns=["target"])
y = heart_data["target"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize the features for better performance of the KNN algorithm
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize lists to store the number of neighbors and corresponding accuracy
neighbors_range = range(1, 251)
accuracies = []

# Evaluate KNN for varying numbers of neighbors
for k in neighbors_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)
    accuracies.append(accuracy_score(y_test, y_pred))

# Find the best and worst performing k values
best_k = neighbors_range[accuracies.index(max(accuracies))]
worst_k = neighbors_range[accuracies.index(min(accuracies))]

print(f"Best k: {best_k} with Accuracy: {max(accuracies):.2f}")
print(f"Worst k: {worst_k} with Accuracy: {min(accuracies):.2f}")

# Plotting accuracy vs. number of neighbors
plt.figure(figsize=(12, 6))
plt.plot(neighbors_range, accuracies, marker="o", linestyle="-", color="b", label="Accuracy")

# Highlight best and worst points
plt.scatter([best_k], [max(accuracies)], color="g", label=f"Best k = {best_k} (Accuracy: {max(accuracies):.2f})", zorder=5)
plt.scatter([worst_k], [min(accuracies)], color="r", label=f"Worst k = {worst_k} (Accuracy: {min(accuracies):.2f})", zorder=5)

# Adding labels and legend
plt.title("K-Nearest Neighbors: Accuracy vs. Number of Neighbors")
plt.xlabel("Number of Neighbors (k)")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.show()
