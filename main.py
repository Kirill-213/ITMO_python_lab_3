# Vasilev Kirill, R3135, ISU_367964, Variant_4

from itertools import combinations   # подключение библиотеки

# создание словаря с предметами
items = {'в': (3, 25),
         'п': (2, 15),
         'б': (2, 15),
         'а': (2, 20),
         #'и': (1, 5),
         'н': (1, 15),
         'т': (3, 20),
         'о': (1, 25),
         'ф': (1, 15),
         #'д': (1, 10),
         'к': (2, 20),
         'р': (2, 20)
         }

max_sum = 0   # сумма всех очков выживания
for i in items: max_sum += items[i][1]   #  нахождение суммы всех очков выживания

bag_col = 3   # количество столбцов
bag_row = 3   # количество строк
init_point = 15   # начальное количество очков
final_point = 0   # конечное кол-во очков
variables_mass = []   # список подходящих по размеру комбинация
final_variable = ''   # итоговая комбинация
sum_point = 0   # вспомогательная переменная
size_point = 0   # кол-во ячеек предмета
max_variable = 0   # максимальная сумма очков комбинации

# находим комбинации в которых размер == bag_row * bag_col
for amount in range(1, len(items) - 1):
    variables = ["".join(map(str, comb)) for comb in combinations(items, amount)]   # создаем список всех комбинаций
    for letter in variables:
        mass = list(letter)
        for i in mass:
           size_point += items[i][0]
        if size_point == bag_row * bag_col:   # проверка условия
            variables_mass.append(letter)   # добавляем подходящие комбинации в список
        size_point = 0

# пробегаем по подходящим вариантам
for i in range(len(variables_mass)):
    for j in list(variables_mass[i]):
        sum_point += items[j][1]
    final_point = sum_point - (max_sum - sum_point)   # находим сумму очков каждого варианта
    sum_point = 0
    if final_point > max_variable:   # отбираем максимальную сумма очков + наилучшую комбинацию
        max_variable = final_point   # максимаьная сумма очков
        final_variable = variables_mass[i]   # наилучшая комбинация

line = ''   # финальный вариант комбинации
for i in list(final_variable): line += items[i][0] * i   # финальная строка с учетом размера каждого предмета

index = 0   # индекс каждой буквы
final  = ''   # финальная строка
# цикл создание итогового списка
for i in range(bag_col):
    for j in range(bag_row):
        final += f'[{line[index]}]'
        if j < (bag_col - 1):
            final += ','
        index += 1
    final += '\n'   # перенос строки

# вывод на экран
print(final)
print('Очки выживания:',final_point + init_point)
