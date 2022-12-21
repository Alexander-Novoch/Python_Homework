# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число : '))

main_n = n
list_of_faktor = []
num_faktor = 2
while n > 1:
    if n % num_faktor == 0:
        list_of_faktor.append(num_faktor)
        n = int(n/num_faktor)
    else:
        num_faktor += 1

print(f'{main_n} = ', end='')
print(*list_of_faktor, sep=" * ")
