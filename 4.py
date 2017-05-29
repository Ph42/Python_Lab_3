#Лаб 3
import random

n = random.randint(11, 9999)

print('Число = {}\nПредпоследняя цифра = {}'.format(n,(n % 100) // 10))
input()