'''
Вася взял игральную кость и написал на гранях числа ...
Для генерации случайного числа Вася решил воспользоваться следующим алгоритмом:
•	Выбрать число ...
•	Подбросить кубик ...
•	Пройтись по списку с конца и вычеркнуть число ...
Определите математическое ожидание суммы оставшихся в последовательности чисел, если Вася сообщит вам числа ...
Обратите внимание, что кубик у Васи честный и все выпадение любой из граней равновероятно. Кроме этого, подбрасывания кубика независимы.
Формат ввода
В первой строке записаны 6 целых чисел ...
Во второй строке записано одно число ...
Формат вывода
Выведите одно вещественное число — требуемое по условию задачи математическое ожидание.
Ответ будет считаться верным, если относительная или абсолютная погрешность не будет превышать 10 ^ (-6)

Примечания
В первом примере из 36 возможных исходов в 6 будет вычеркнуто повторяющееся число.
Во втором примере возможна единственная последовательность 2 2 2, после вычеркивания двух двоек длина последовательности станет равной одному.
'''

import random
from itertools import product

def expected_sum(dice_faces, k):
    dp = [[0] * 6 for _ in range(2)]
    count = [[0] * 6 for _ in range(2)]

    # Инициализация начальных состояний
    for face in range(6):
        dp[0][face] = dice_faces[face]
        count[0][face] = 1

    # Заполнение dp по шагам
    for step in range(1, k):
        for curr in range(6):
            dp[step % 2][curr] = 0
            count[step % 2][curr] = 0
            for prev in range(6):
                # Учитываем добавление числа, если оно не равно предыдущему
                if dice_faces[curr] != dice_faces[prev]:
                    dp[step % 2][curr] += dp[(step - 1) % 2][prev] + dice_faces[curr] * count[(step - 1) % 2][prev]
                else:
                    dp[step % 2][curr] += dp[(step - 1) % 2][prev]
                count[step % 2][curr] += count[(step - 1) % 2][prev]

    # Суммируем результаты
    total_sum = sum(dp[(k - 1) % 2])
    total_count = sum(count[(k - 1) % 2])

    return total_sum / total_count


# Ввод данных
dice_faces = list(map(int, input().split()))
k = int(input())

# Вычисление результата
result = expected_sum(dice_faces, k)
print(f"{result:.10f}")


# numbers = [random.randint(1, 10) for i in range(6)]
# print(f'numbers: {sorted(numbers)}')
#
# k = random.randint(2, 3)
# print(f'k: {k}')
#
# if k == 1:
#     print(sum(numbers) / 6)
# else:
#     res1 = {key: [key, 1] for key in numbers}
#     res2 = {}
#     for key, value in res1.items():
#         for num in numbers:
#             if num != value[0]:
#                 res_ = key + num
#                 if res_ in res2:
#                     res[res_][0], res[res_][1] =


#--------------------------------------------------------------------------------------
# from itertools import product
#
# numbers = list(map(int, input().split()))
#
# k = int(input())
#
# summ = 0
# if k != 1:
#     combinations = [list(comb) for comb in product(numbers, repeat = k)]
#     for combination in combinations:
#         flag = 1
#         for i in range(1, k):
#             if combination[i] == combination[i - flag]:
#                 flag += 1
#                 combination[i] = 0
#         summ += sum(combination)
#     v = summ / len(combinations)
# else:
#     mathematical_expectation = sum(numbers) / 6
#
# print(mathematical_expectation)