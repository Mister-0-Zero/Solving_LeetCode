# import random
# import time
#
# def solve():
#     def function(parameter, flag_index):
#         i = len(mass) - 1
#         while True:
#             if mass[i] == parameter:
#                 if flag_index < i:
#                     return sum(mass[flag_index:i + 1]), [flag_index, i]
#                 else:
#                     return sum(mass[i:flag_index + 1]), [flag_index, i]
#                 break
#             else:
#                 i -= 1
#
#
#     if len(mass) == 1:
#         print(*mass)
#     else:
#         mx = max(mass)
#         mn = min(mass)
#         i = 0
#         while True:
#             if mass[i] in (mx, mn):
#                 if mx == mass[i]: flag = 1
#                 else: flag = 2
#                 flag_index = i
#                 break
#             else:
#                 i += 1
#         res1 = function(mn if flag == 1 else mx, flag_index)
#
#         i = flag_index
#         if flag == 1:
#             while True:
#                 if mass[i] == mn:
#                     flag = 2
#                     flag_index = i
#                     break
#                 else:
#                     i += 1
#         else:
#             while True:
#                 if mass[i] == mx:
#                     flag = 1
#                     flag_index = i
#                     break
#                 else:
#                     i += 1
#         res2 = function(mn if flag == 1 else mx, flag_index)
#         return res1 if res1[0] > res2[0] else res2
#
# def solve_stupid():
#     mx = max(mass)
#     mn = min(mass)
#     mass_ind_mn = []
#     mass_ind_mx = []
#     for ind, el in enumerate(mass):
#         if el == mn: mass_ind_mn.append(ind)
#         if el == mx: mass_ind_mx.append(ind)
#     max_sum = 0
#     for mn_ind in mass_ind_mn:
#         for mx_ind in mass_ind_mx:
#             if mx_ind > mn_ind:
#                 summ = sum(mass[mn_ind:mx_ind + 1])
#             else:
#                 summ = sum(mass[mx_ind:mn_ind + 1])
#             if summ > max_sum:
#                 max_sum = summ
#                 indexs = [mx_ind, mn_ind]
#     return max_sum, indexs
#
# while True:
#     n = random.randint(10000, 100000)
#     mass = [random.randint(1, 1000) for i in range(n)]
#     print()
#     # print(n, mass)
#     c = time.time()
#     res1 = solve()
#     print(time.time() - c)
#     c = time.time()
#     res2 = solve_stupid()
#     print(time.time() - c)
#     print(res1)
#     print(res2)
#     if res1[0] != res2[0]:
#         break

n = int(input())
mass = list(map(int, input().split()))


def calculate_sum(param, start_index):
    for i in range(len(mass) - 1, -1, -1):
        if mass[i] == param:
            return sum(mass[min(start_index, i):max(start_index, i) + 1])


if len(mass) == 1:
    print(mass[0])
else:
    mx = max(mass)
    mn = min(mass)

    first_index = next(i for i, x in enumerate(mass) if x in (mx, mn))
    first_flag = mn if mass[first_index] == mx else mx

    res1 = calculate_sum(first_flag, first_index)

    second_index = next(i for i in range(first_index + 1, len(mass)) if mass[i] == first_flag)
    second_flag = mn if mass[second_index] == mx else mx

    res2 = calculate_sum(second_flag, second_index)

    print(max(res1, res2))