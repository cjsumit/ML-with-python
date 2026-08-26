# datasets = [
#     [75,80,85],
#     [80,75,90],
#     [70,95,85]
# ]
# columns = p | c | m
# 1. Total marks by each student.
# (draw a bar graph for this)
# 2. Average makrs of each subject and compare it from the marks of each stuent in that subject
# (plot a line graph for this)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dataset
datasets = [
    [75, 80, 85],
    [80, 75, 90],
    [70, 95, 85]
]

# Create DataFrame
columns = ['P', 'C', 'M']
df = pd.DataFrame(datasets, columns=columns, index=['Student 1', 'Student 2', 'Student 3'])

print(df)

# ------------------------------------------------
# 1. Total marks by each student - Bar Graph
# ------------------------------------------------

total_marks = df.sum(axis=1)

print("\nTotal marks:")
print(total_marks)

plt.figure(figsize=(7, 5))
plt.bar(total_marks.index, total_marks.values)

plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Total Marks of Each Student")

plt.show()


# ------------------------------------------------
# 2. Subject average vs each student's marks
#    - Line Graph
# ------------------------------------------------

subject_average = df.mean(axis=0)

print("\nAverage marks of each subject:")
print(subject_average)

plt.figure(figsize=(8, 5))

# Marks of each student
plt.plot(df.columns, df.loc['Student 1'], marker='o', label='Student 1')
plt.plot(df.columns, df.loc['Student 2'], marker='o', label='Student 2')
plt.plot(df.columns, df.loc['Student 3'], marker='o', label='Student 3')

# Subject average
plt.plot(
    df.columns,
    subject_average,
    marker='o',
    linestyle='--',
    label='Subject Average'
)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks vs Subject Average")
plt.legend()
plt.grid(True)

# Maximum marks in each subject
max_marks = df.max(axis=0)

# Minimum marks in each subject
min_marks = df.min(axis=0)

print("\nMaximum marks in each subject:")
print(max_marks)

print("\nMinimum marks in each subject:")
print(min_marks)

# Bar graph
x = np.arange(len(columns))
width = 0.35

plt.figure(figsize=(8, 5))

plt.bar(x - width/2, max_marks, width, label='Maximum Marks')
plt.bar(x + width/2, min_marks, width, label='Minimum Marks')

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Maximum and Minimum Marks in Each Subject")
plt.xticks(x, columns)
plt.legend()
plt.grid(axis='y')

plt.show()