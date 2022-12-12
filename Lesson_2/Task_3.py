# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#     *Пример:*
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.

number = int(input('Введите целое число n= '))
number_list = {}
sum = 0
for i in range(1, number + 1):
    number_list[i] = round((1+(1/i)) ** i, 3)
    sum += number_list[i]
print(number_list)
print(f'Сумма значений = {round(sum,3)}')
