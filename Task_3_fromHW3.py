def check_for_input_error():
    while True:
        try:
            a = list(map(float, input('Введите несколько вещественных чисел через пробел: ').split(' ')))
        except ValueError:
            print('Ошибка - введено не числовое значение!')
            continue
        return a
floor_collection = [i % 1 for i in check_for_input_error()]
print(f'Разница между максимальным и минимальным значениями дробной части элементов списка = {max(floor_collection) - min(floor_collection)}')