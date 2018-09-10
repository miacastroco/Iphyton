import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import time

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

points = []

for i in range(5,20):
  Fib = 0
  temp = 0
  num = 1
  num2 = 1
  in1 = i
  inp = in1-2
  while inp>0:
    temp = num
    num = num + num2
    num2 = temp
    inp = inp-1
  Fib = num
  print (str(Fib))
  points.append(Fib)

plt.plot(points)
plt.show()
ax.plot(points)
fig.savefig('graph.png')
