#Лаб 3
import random
import math
n = int(input('Введите количество членов последовательности\n\tn = '))
x = float(input('Введите x\n\tx = '))
s = 0
EstChisla = False
if n >= 1:
	EstChisla = True
	for i in range(1, n+1):
		s += (2*x)**(i-1) / math.factorial(i-1)

if EstChisla:
	print('Сумма членов последовательности\n\t= {:.2f}'.format(s))
else:
	print('Нет чисел в последовательности')
input()