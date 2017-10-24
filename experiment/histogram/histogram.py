import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Reading student data from an input file
with open("student-data.txt", "r") as f:
    lines = map(int, f.read().split())

counts = Counter(lines) # Counter will keep track of how many times equivalent values are present in file
hoursSpent, students = zip(*counts.items()) # separating key-pair values

# plotting data into bubble chart
sizes = np.array(counts.values())**2
plt.scatter(hoursSpent, students, s=sizes, marker='o', c=sizes)

# add labels
plt.xlabel('time spend for corrections')
plt.ylabel('number of students')

# adding x and y axis indices
plt.xticks(hoursSpent)
plt.yticks(students)

# Display the chart
plt.show()
