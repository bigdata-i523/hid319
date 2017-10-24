import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Reading student data from an input file
with open("student-data.txt", "r") as f:
    lines = map(int, f.read().split())

counts = Counter(lines)  # Counter will keep track of how many times equivalent values are present in file
workCategory, workItems = zip(*counts.items())  # separating key-pair values


overallWorkItems = []
j = len(workCategory)
for i in range(j):
    items = workCategory[i]*workItems[i]
    overallWorkItems.append(items)

# plotting data into bubble chart
sizes = np.array(overallWorkItems)**1.5
plt.scatter(workCategory, overallWorkItems, s=sizes, marker='o', c=sizes)

# adding labels
plt.xlabel('Work Category')
plt.ylabel('Number of Work Items')
plt.title('Student Work Log')

# adding x and y axis indices
plt.xticks(workCategory)
plt.yticks(overallWorkItems)

# Display the chart
plt.show()
