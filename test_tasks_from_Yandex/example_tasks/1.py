'''
Петя написал два генератора точек в круге:

def generate1():
    a = uniform(0, 1)
    b = uniform(0, 1)
    return (a * cos(2 * pi * b), a * sin(2 * pi * b))

def generate2():
    while True:
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)
Даны 100 наборов по 1000 точек, каждый набор сгенерирован каким-то одним из этих двух алгоритмов. Необходимо определить для каждого набора, первый или второй алгоритм использовался для его генерации.
Для того, чтобы получить ОК по этой задаче, надо предсказать правильный генератор хотя бы для 98 наборов.
Формат ввода
Даны 100 строк. Каждая строка отвечает за свой набор точек.
В каждой строке находится 2000 действительных чисел (−1≤ai≤1−1≤ai≤1), разделённых пробелом. Точки идут подряд, то есть формат строки: x0 y0 x1 y1 x2 y2 ... x999 y999
Формат вывода
Нужно вывести 100 строк, в каждой из которой должно быть 1 число: 1 или 2, в зависимости от того, первым или вторым генератором был сгенерирован данный набор точек.
'''
import random
from math import cos, sin, pi
import matplotlib.pyplot as plt


def generate1():
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    return (a * cos(2 * pi * b), a * sin(2 * pi * b))


def generate2():
    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)


def generate_point():
    mass_pointers = []

    if random.randint(0, 1):
        num_generate = 1
        while len(mass_pointers) != 2000:
            x, y = generate1()
            mass_pointers.append(x)
            mass_pointers.append(y)
    else:
        num_generate = 2
        while len(mass_pointers) != 2000:
            x, y = generate2()
            mass_pointers.append(x)
            mass_pointers.append(y)

    return num_generate, mass_pointers

def determine_generator(mass_pointers):
    intervals = [0, 0]
    for i in range(1000):
        x, y = mass_pointers[i * 2], mass_pointers[i * 2 + 1]
        if x ** 2 + y ** 2 <= 0.5:
            intervals[0] += 1
        else:
            intervals[1] += 1
    if intervals[0] > intervals[1] * 1.2:
        return 1
    else:
        return 2

fig, axes = plt.subplots(2, 5, figsize=(15, 6))

axes = axes.ravel()

for i in range(10):
    num_generate, mass_pointers = generate_point()

    for I in range(1000):
        x, y = mass_pointers[I * 2], mass_pointers[I * 2 + 1]
        axes[i].scatter(x, y, color='red', s=1)

    axes[i].set_title(f'Генератор {num_generate}')
    axes[i].grid()

plt.tight_layout()

plt.show()

score = 1
for i in range(100):
    num_pre, mass_pointers = generate_point()
    res = determine_generator(mass_pointers)
    if num_pre == res:
        score += 1
    print(res, num_pre == res)
print(score)

#------------------------------------------------------------------------------------------------------------------

# def determine_generator(mass_pointers):
#     intervals = [0, 0]
#     for i in range(1000):
#         x, y = mass_pointers[i * 2], mass_pointers[i * 2 + 1]
#         if x ** 2 + y ** 2 <= 0.5:
#             intervals[0] += 1
#         else:
#             intervals[1] += 1
#     if intervals[0] > intervals[1] * 1.2:
#         return 1
#     else:
#         return 2
#
# for i in range(100):
#     mass_pointers = list(map(float, input().split()))
#     res = determine_generator(mass_pointers)
#     print(res)