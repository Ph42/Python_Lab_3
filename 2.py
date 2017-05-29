#Лаб 3 - Оператор цикла с параметром
import random
import math
n = int(input('Введите целое n \n\t n = '))
k = 1
s = 0
while k <= n:
	s += ((-1)**k * (k**3 - 27)) / (3*math.factorial(k+2))
	k += 1
print('S = {:.6f}'.format(s))
input()