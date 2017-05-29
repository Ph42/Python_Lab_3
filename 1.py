#Лаб 3 - Оператор цикла с параметром
import random

d = random.uniform(0, 2)

a1 = 1
a2 = 2
an = 0
k = 2
while abs(a2 - a1) >= d:
	a1, a2 = a2, (a2 + a1)/2
	k += 1
print ('D = ',d,'\nK = ',k,'\nAK-1 = ',a1,'\nAK = ',a2)
input()