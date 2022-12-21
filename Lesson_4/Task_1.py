# Вычислить число Пи c заданной точностью d
# Пример:
# - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

import math

d = str(input('Введите точность числа ПИ : '))
print(math.pi)
d_len = len(d.split('.')[1])

i = 0
num_pi = str(math.pi)
while i < (d_len+2) and i < len(num_pi):
    print(num_pi[i], end="")
    i += 1
