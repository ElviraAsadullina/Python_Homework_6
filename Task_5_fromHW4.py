def get_correct_format_polynomial(my_string):
    my_string = my_string.replace(' ', '').replace('+x^', '+1x^').replace('-x^', '-1x^').replace('x+', 'x^1+').replace('x-', 'x^1-').replace('=0', 'x^0=0')
    my_string = my_string.replace('-', '+-').replace('x^', '+')[:-2]
    my_list = my_string.split('+')
    return my_list
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
def get_sum_coefficient(my_list1, my_list2):
    final = []
    for i in range(0, len(my_list1) - 1):
        for j in range(0, len(my_list2) - 1, 2):
            if my_list1[i + 1] == my_list2[j + 1]:
                final.append(my_list1[i] + my_list2[j])
                final.append(my_list1[i + 1])
                i += 2
            else:
                if my_list1[i + 1] > my_list2[j + 1]:
                    final.append(my_list1[i])
                    final.append(my_list1[i + 1])
                    i += 2
                if my_list2[j + 1] not in my_list1:
                    final.append(my_list2[j])
                    final.append(my_list2[j + 1])
                else:
                    final.append(my_list2[j])
                    final.append(my_list2[j + 1])
                    j += 1
        if len(final) >= my_list1[1]:
            break
    return final
with open('for_Task_5_1.txt', 'r', encoding="utf8") as data:
    equality_1 = data.readline()
with open('for_Task_5_2.txt', 'r', encoding="utf8") as data:
    equality_2 = data.readline()
equality_1 = ([int(x) for x in get_correct_format_polynomial(equality_1)])
equality_2 = ([int(x) for x in get_correct_format_polynomial(equality_2)])
final_list = get_sum_coefficient(equality_1, equality_2)
numbers_list = [final_list[i] for i in range(0, len(final_list)) if i % 2 == 0]
degree_list = [final_list[i] for i in range(0, len(final_list)) if i % 2 != 0]
numbers_list = add_plus_for_positive(numbers_list)
x_list = ['x^' for i in range(len(degree_list))]
polynomial = str(get_polynomial_zero_exclude(numbers_list, x_list, degree_list))
chars_to_delete = [",", "[", "]", " ", "'", "x^0"]
for character in chars_to_delete:
    polynomial = polynomial.replace(character, '').replace("^1-", '-').replace("^1+", '+').replace("+1x", '+x').replace("-1x", '-x')
polynomial += '=0'
print(f'Результат суммирования считанных многочленов: {polynomial}')
my_file = open("Answer_for_Task_5.txt", "w")
my_file.write(polynomial)
my_file.close()