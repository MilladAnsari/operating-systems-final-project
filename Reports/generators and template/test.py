import matplotlib.pyplot as plt

# Example dictionary
data = {
    'Apples': 10,
    'Bananas': 15,
    'Cherries': 7,
    'Dates': 12
}

# Extract keys and values
keys = list(data.keys())
values = list(data.values())

# Plot
plt.figure(figsize=(8, 5))
plt.bar(keys, values, color='skyblue', edgecolor='black')

plt.title('Fruit Quantities')
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.grid(axis='y', alpha=0.7)
plt.tight_layout()
plt.show()
