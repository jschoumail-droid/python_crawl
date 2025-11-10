'''employees=[['John',38,'Sales'],['Lisa',28,'Marketing'],['Sujan',33,'HR']]
employee=employees[1]
print(employees)
print(employee)
print('name:',employee[0])
print('age:',employee[1])'''

employees=[
    {'Name':'John','Age':38,'Department':'Sales'},
    {'Name':'Lisa','Age':28,'Department':'Marketing'},
    {'Name':'Sujan','Age':28,'Department':'HR'}
    ]
print(employees)
'''for employee in employees:
    print('Name:',employee['Name'])
    print('Age:',employee['Age'])
    print('Department:',employee['Department'])
    print('-'*20)'''

for employee in employees:
    if employee['Name']=='Sujan':
        print('Name:',employee['Name'])
        print('Age:',employee['Age'])
        print('Department:',employee['Department'])
        print('-'*20)
