import matplotlib.pyplot as plt

hours = [4, 8, 2]

activites = ['Sleep' , 'work', 'play']
colors = ['gold', 'silver', 'red']


plt.pie(hours, labels=activites, colors=colors, startangle=60, autopct='%.1f%%')

plt.show()