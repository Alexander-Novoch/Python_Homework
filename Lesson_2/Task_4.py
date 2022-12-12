# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

#Этот вариант почему-то у меня не заработал

# n = int(input('Введите число n= '))
# list_n = []
# for i in range(-abs(n), abs(n) + 1):
#     list_n.append(i)
# print(list_n)

# prod = 1
# path = 'file.txt'
# with open(path, 'r') as data:
#     for line in data:
#         prod *= list_n[int(line)]
#     print(prod)
#---------------------------------------------------

def find_product_ininterval(n, m, p):


    if m > 2*n or p > 2*n:
        print("index cant be more than interval")
        exit()

    interval_nminusn = range(-n, n + 1)

    data_write = open('file.txt', 'w')
    for i in interval_nminusn:
        data_write.write(str(i) + '\n')
    data_write.close()

    data_read = open('file.txt', 'r')
    string_of_interval = (data_read.read()).split()
    data_read.close()

    print(f"{string_of_interval[m]}(index{m}){string_of_interval[p]}(index{p})={int(string_of_interval[m]) + int(string_of_interval[p])}")


find_product_ininterval(5, 7, 4)
