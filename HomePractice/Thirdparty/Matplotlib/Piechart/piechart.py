import matplotlib.pyplot as plt

labels=['Monica','Adrian','Jared']
num=[230,100,98]

plt.title('Voting Result: Club President',fontdict={'fontsize':20})
plt.pie(num,labels=labels,autopct='%1.1f%%',colors=['lightblue','lightgreen','yellow'])
plt.show()