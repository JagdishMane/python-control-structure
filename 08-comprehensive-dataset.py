import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)


# Function to calculate average value of a list
def calculate_average(numbers):
    """
    Calculate the average value of a list of numbers.
    Parameters:
    numbers (list): A list of numeric values.
    Returns:
    float: The calculated average value. If the list is empty, returns 0.
    """
    total = sum(numbers)
    count = len(numbers)
    if count > 0:
        return total / count
    else:
        return 0
    
# Calculate the average alcohol content of wine
alcohol_column = df['alcohol'] # Corrected index for age column
average_alcohol = calculate_average(alcohol_column)
print(f"Average age of patients: {average_alcohol:.2f}")

# Loop to find wines with flavanoids above a certain threshold
flavanoids = df['flavanoids']
flav_threshold = 1.5
wines_above_threshold = []
for i in range(len(flavanoids)):
    if flavanoids[i] > flav_threshold: # Corrected comparison
        wines_above_threshold.append(i)
print(f"Number of wines with flavanoids above {flav_threshold}:,→{len(wines_above_threshold)}")

highest_alcohol_index = 0
highest_alcohol = df['alcohol'][highest_alcohol_index]
i = 1
while i < len(df):
    if df['alcohol'][i] > highest_alcohol:
        highest_alcohol = df['alcohol'][i]
        highest_alcohol_index = i
    i += 1
print(f"Highest alcohol content: {highest_alcohol:.2f}% for wine at index ,→{highest_alcohol_index}")


if average_alcohol > 10:
    print("The average alcohol of wines is higher than 10.")
else:
    print("The average alcohol of wines is not higher than 10.")

subset_size = 5
print("\nSubset of wine data:")
for i in range(subset_size):
    print(f"Wine {i + 1}: Alcohol {df['alcohol'][i]:.2f}%,"
        f" Flavanoids {df['flavanoids'][i]:.2f},"
        f" Proline {df['proline'][i]:.2f}")
    
# Subset of wine data:
# Wine 1: Alcohol 14.23%, Flavanoids 3.06, Proline 1065.00
# Wine 2: Alcohol 13.20%, Flavanoids 2.76, Proline 1050.00
# Wine 3: Alcohol 13.16%, Flavanoids 3.24, Proline 1185.00
# Wine 4: Alcohol 14.37%, Flavanoids 3.49, Proline 1480.00
# Wine 5: Alcohol 13.24%, Flavanoids 2.69, Proline 735.00
# 10
