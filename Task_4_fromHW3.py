def check_for_input_error():
    while True:
        try:
            a = int(input('Введите число в десятичном формате: '))
        except ValueError:
            print('Ошибка - введено не числовое значение!')
            continue
        return a
number = check_for_input_error()
print(f'Введенное число в двоичном формате: {int(bin(number)[2:])}')