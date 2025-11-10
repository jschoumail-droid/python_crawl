employee={"name":"Jack", "age":32, "department":"sales"}
#print(employee["age"])

employee["department"]="civil"
#print(employee)

employee={}
employee['name']='johnson'
employee['department']='pipe'
employee["age"]=25
employee["year"]=2005
employee["year"]=employee["year"]+6

employee["other"]={"company":'CEC','year':5}
#print(employee)

for key in employee:
    print(employee[key])

'''del employee["other"]
print(employee)'''

#item=employee.pop('other')
item=employee.popitem()
print(item,employee)
print(len(employee))
print(sorted(employee))

employee.clear()
print(type(employee),employee)

employee=dict([(1,'joe'),(2,'mary'),(3,'hook')])
print(employee)

key='name'
print(key,employee.get(key,'not found'))

keys=employee.keys()
print(keys)

lst1=list(keys)
for e in lst1:
    print(e, end=' ')
print()

print(1 in employee)
print(4 in employee)
