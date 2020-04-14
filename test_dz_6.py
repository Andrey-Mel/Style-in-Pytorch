#первая функция для тестирования простые числа
def f_prost_chisla(n):
    digit = []
    for i in range(2, n+1 ):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            digit.append(i)
    return f'Простые числа введеного числа \n {digit}'    # вывод простых чисел


def f_prost_chisla_test(n):
    '''
    На вход нужны числа только положитльные и не str
    :return:
    '''
    if type(n) is not int:
        return f'Число не должно быть текст'
    elif 0 <= n <= 1:
        return f'Число должно быть больше 0 и 1'
    else:
        return f_prost_chisla(n)

#print(f_prost_chisla_test(1))

# Вторая функция на тестирование
def travel (country_num):
    if country_num == 1:
        return f'Turkey'
    elif country_num == 2:
        return f'USA'
    elif country_num == 3:
        return f'Russia'

#print(travel(3))

def travel_country_test(country_num):
    country_num_list = [1, 2, 3]
    if type(country_num) is not int:
        raise TypeError('Введите число')
    elif country_num not in country_num_list:
        raise ValueError('Такой страны в списке нет')
    else:
        return travel(country_num)

#print(travel_country_test(1))

#функция для try
def password():
    try:
        passw = int(input('Введите пароль только цифры '))
        if passw == 1234:
            print('Вы угадали')
    except ValueError:
        print('Не тот тип данных - нужны цифры')
    else:
        print('Блок else Число угадано')
    finally:
        print('End')

#password()



## тест с помощью pytest
def f_mnogitely(n):
    print(f' Вы ввели число {n}')
    Mnogitely = []
    j = 2
    while j <= n:
        if n % j == 0:
            Mnogitely.append(j)
            n //= j
        else:
            j += 1

    if n > 1:
       Mnogitely.append(n)
    return Mnogitely
print(f_mnogitely(144))

def test_1_f_mnogitely():
    assert f_mnogitely(144) == [2, 2, 2, 2, 3, 3]
#Умышленно не рабочее
# def test_2_f_mnogitely():
#     assert f_mnogitely(144) == [2, 2, 2, 3, 3, 3]

# Проверка на длину списка множителей числа 144
def test_3_f_mnogitely():
    assert len(f_mnogitely(144)) == 6