import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import time

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

points = []
Ttime=0
for i in range(0,50):
  start = time.time()
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
  end = time.time()
  print (str(Fib))
  Ttime = Ttime + (end-start)
  points.append(Ttime)
  
print ("Int = 93th para overflow, aunque se puede aumentar el limite por memoria")
plt.plot(points)
plt.show()
ax.plot(points)
fig.savefig('graph.png')
