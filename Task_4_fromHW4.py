def check_for_input_error():
    while True:
        try:
            a = int(input('Задайте максимальную степень для многочлена: '))
        except ValueError:
            print('Ошибка - необходимо ввести натуральное число!')
            continue
        if  a < 1:
            print('Ошибка - число должно быть положительным!')
            continue
        break
    return a
def add_plus_for_positive(my_list):
    for i in range(1, len(my_list), 1):
        if my_list[i] > 0:
            my_list[i] = f'{my_list[i]:+}'
    return my_list
def get_polynomial_zero_exclude(my_list1, my_list2, my_list3):
    polynomial = []
    length = len(my_list1)
    for i, j, k in zip(my_list1, my_list2, my_list3):
        my_list1 = iter(range(length))
        my_list2 = iter(range(length))
        my_list3 = iter(range(length))
        if i == 0:
            next(my_list3)
            next(my_list1)
            next(my_list2)
        elif i == 1 and k != 0:
            polynomial += [j, k]
        else:
            polynomial += [i, j, k]
    return polynomial
k = check_for_input_error()
degree_list = list(range(0, k + 1))
degree_list.reverse()
x_list = list('x^' for i in range(len(degree_list)))
from random import randint
numbers_list = add_plus_for_positive([randint(-100, 101) for i in range(len(degree_list))])
polynomial = str(get_polynomial_zero_exclude(numbers_list, x_list, degree_list))
chars_to_delete = [",", "[", "]", " ", "'", "x^0"]
for character in chars_to_delete:
    polynomial = polynomial.replace(character, '').replace("^1-", '-').replace("^1+", '+').replace("+1x", '+x').replace("-1x", '-x')
polynomial += '=0'
print(f'Полученный многочлен: {polynomial}')
my_file = open("for_Task_4.txt", "w")
my_file.write(polynomial)
my_file.close()