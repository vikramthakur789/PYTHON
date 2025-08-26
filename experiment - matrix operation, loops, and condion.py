import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print('Addition:\n',A + B)
print('Subtraction:\n',A -B)
print('Element-wise Multiplication:\n',A * B)
print('Matrix Multiplication:\n',A @ B)
print('Transpose:\n',A.T)
for i in np.nditer(A):
  if i % 2 == 0:
    print(f'{i} is even')
  else:
    print(f'{i} is odd')
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,1,8,7]
plt.plot(x,y,color='green', linestyle='--',marker='o')
plt.title('Sample Line Plot')
plt.xlabel('X-Axis')
plt.xlabel('Y-Axis')
plt.grid(True)
plt.show()
names = ['A','B','C','D']
scores = [23,45,56,78]
plt.bar(names, scores, color='orange')
plt.title('Bar Chart')
plt.ylabel('Scores')
plt.show()
data = [22,87,5,43,56,73,55,54,11,20,51,5,79]
plt.hist(data, bins=5, color='purple')
plt.title('Histogram')
plt.show()
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df['species'].value_count())
print(df.isnull().sum())
filtered = df[df['petal_length']>1.5]
print(filtered)
