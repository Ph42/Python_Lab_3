#Лаб 3
import random

ishodnayaSummaVklada = 24
procent = 0.06
godSozdaniyaVklada = 1826
tekushiiGod = 2017
summaVklada = ishodnayaSummaVklada
for i in range(godSozdaniyaVklada + 1, tekushiiGod):
	summaVklada += summaVklada*procent
print('Состояние поселенцев, не купивших Манхэттен, а создавших вклад в банке,\nна сегодняшний день минимум:\n\t = {:.2f}$'.format(summaVklada))
input()