employees=[["Joe",38,"Sales"],["Lisa",29,"Marking"],["Sujan"],33,"HR"]
print(employees)
print(employees[1])

animals=['cat','dog','bat']
for index,animal in enumerate(animals):
    print(index,animal)

for index in enumerate(animals):
    print(index)

#initial marix m23
intRow=2
intCol=3
m=[[0]*intCol for row in range(intRow)]
print(m)