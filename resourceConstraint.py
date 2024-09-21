from pulp import *

# Define the number of classes and teachers
num_classes = 10
num_teachers = 5

# Define the maximum workload for each teacher
max_workload = [2, 3, 4, 2, 3]

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Class Distribution Problem", LpMinimize)

# Define the variables
teacher_vars = LpVariable.dicts("Teacher", [(i, j) for i in range(num_teachers) for j in range(num_classes)], 0, 1,
                                LpBinary)

# Define the objective
prob += lpSum([teacher_vars[(i, j)] for i in range(num_teachers) for j in range(num_classes)])

# Define the constraints
for j in range(num_classes):
    prob += lpSum([teacher_vars[(i, j)] for i in range(num_teachers)]) == 1

for i in range(num_teachers):
    prob += lpSum([teacher_vars[(i, j)] for j in range(num_classes)]) <= max_workload[i]

# Solve the problem
prob.solve()

# Print the results
for i in range(num_teachers):
    for j in range(num_classes):
        if teacher_vars[(i, j)].varValue == 1:
            print("Teacher", i, "teaches class", j)
