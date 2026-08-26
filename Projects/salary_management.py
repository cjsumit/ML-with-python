# Questions / Tasks
# 1. How will you calculate the average salary of all employees?
# 2. How will you find the highest salary?
# 3. How will you find the lowest salary?
# 4. How will you calculate the average experience?
# 5. How will you find employees whose salary is greater than ₹40,000?
# 6. How will you find employees whose performance score is greater than 80?
# 7. How will you find the employee with the highest performance score?
# 8. How will you calculate the standard deviation of salaries?
# 9. How will you classify employees as High Salary or Low Salary using np.where()?
# 10. How will you convert the results into a Pandas DataFrame?

import numpy as np
import pandas as pd

employees = np.array([
    ["Amit", 40000, 3, 75],
    ["Rahul", 50000, 5, 85],
    ["Priya", 35000, 2, 90],
    ["Neha", 60000, 7, 95],
    ["Ravi", 45000, 4, 70]
])

salary = employees[:, 1].astype(float)
experience = employees[:, 2].astype(float)
performance = employees[:, 3].astype(float)

# 1. Average salary
print("Average Salary:", np.mean(salary))

# 2. Highest salary
print("Highest Salary:", np.max(salary))

# 3. Lowest salary
print("Lowest Salary:", np.min(salary))

# 4. Average experience
print("Average Experience:", np.mean(experience))

# 5. Salary greater than 40000
print("Salary > 40000:")
print(employees[salary > 40000])

# 6. Performance greater than 80
print("Performance > 80:")
print(employees[performance > 80])

# 7. Highest performance employee
index = np.argmax(performance)
print("Highest Performance Employee:", employees[index])

# 8. Standard deviation
print("Salary Standard Deviation:", np.std(salary))

# 9. Salary classification
salary_category = np.where(
    salary >= 40000,
    "High Salary",
    "Low Salary"
)

# 10. Pandas DataFrame
df = pd.DataFrame({
    "Name": employees[:, 0],
    "Salary": salary,
    "Experience": experience,
    "Performance": performance,
    "Salary Category": salary_category
})

print("\nDataFrame:")
print(df)


