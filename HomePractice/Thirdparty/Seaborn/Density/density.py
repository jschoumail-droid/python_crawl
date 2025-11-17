import seaborn as sns
import matplotlib.pyplot as plt

data=[90,80,50,42,89,78,34,70,67,73,74,80,60,90,90]

plt.title('Density Plot')
plt.xlabel('Score')
plt.ylabel('Density')
sns.distplot(data)
plt.show()