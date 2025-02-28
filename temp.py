import matplotlib.pyplot as plt

# Sample data
data = {'X1': 99, 'X2': 95, 'X3': 96, 'X4': 89}

# Extracting column names and corresponding values
columns = list(data.keys())
values = list(data.values())

# Creating a bar plot
plt.bar(columns, values, color=['blue', 'green', 'orange', 'red'])
plt.xlabel('Columns')
plt.ylabel('Values (%)')  # Assuming values are percentages
plt.title('Plot with Columns X1, X2, X3, X4')

# Displaying y-axis labels as percentages
plt.gca().set_yticklabels(['{:.0f}%'.format(val) for val in plt.gca().get_yticks()])

# Adding values on top of each bar
for i, value in enumerate(values):
    plt.text(i, value + 1, f'{value}%', ha='center', va='bottom')

plt.show()
