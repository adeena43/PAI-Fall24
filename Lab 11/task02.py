# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
file_path = "heart.csv"  
heart_data = pd.read_csv(file_path)

# Separate features (X) and target (y)
X = heart_data.drop(columns=["target"])
y = heart_data["target"]

# Standardize the features for better performance of the KNN algorithm
scaler = StandardScaler()

# Initialize a dictionary to store accuracies for each random seed
seed_accuracies = {}

# Range of neighbors
neighbors_range = range(1, 251)

# Run the KNN algorithm for random seed values from 1 to 10
for seed in range(1, 11):
    # Split the dataset into training and testing sets with the current seed
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed, stratify=y
    )
    
    # Standardize the features
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Initialize a list to store accuracies for the current seed
    accuracies = []
    
    # Evaluate KNN for varying numbers of neighbors
    for k in neighbors_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_scaled, y_train)
        y_pred = knn.predict(X_test_scaled)
        accuracies.append(accuracy_score(y_test, y_pred))
    
    # Store the best accuracy for the current seed
    seed_accuracies[seed] = max(accuracies)

# Print all accuracies for different seeds
print("Accuracies for each random seed:")
for seed, accuracy in seed_accuracies.items():
    print(f"Seed {seed}: {accuracy:.2f}")

# Find the highest and lowest accuracy across all seeds
highest_seed = max(seed_accuracies, key=seed_accuracies.get)
lowest_seed = min(seed_accuracies, key=seed_accuracies.get)

print(f"\nHighest Accuracy: {seed_accuracies[highest_seed]:.2f} (Seed {highest_seed})")
print(f"Lowest Accuracy: {seed_accuracies[lowest_seed]:.2f} (Seed {lowest_seed})")
