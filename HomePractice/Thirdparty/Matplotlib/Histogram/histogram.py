import matplotlib.pyplot as plt

grades=['A','B','C','D','E','F']
studentCount=[20,30,10,5,8,2]

plt.xlabel('Grade')
plt.ylabel('Num Students')
#plt.bar(grades,studentCount,color=['green','gray','gray','gray','gray','red'])
plt.barh(grades,studentCount,color=['green','gray','gray','gray','gray','red'])
plt.show()