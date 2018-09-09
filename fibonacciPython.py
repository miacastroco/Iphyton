#Fibonacci Python
Fib = 0
temp = 0
num = 1
num2 = 1
in1 = int(input("Ingrese el numero de fibonacci "))
inp = in1-2
while inp>0:
	temp = num
	num = num + num2
	num2 = temp
	inp = inp-1
Fib = num
print Fib
