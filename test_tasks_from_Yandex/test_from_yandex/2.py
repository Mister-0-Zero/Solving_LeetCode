# input_value = list(map(int, input().split()))
# n, m, k = input_value[0], input_value[1], input_value[2]
#
# mass_beds = sorted(list(map(int, input().split())))
#
# try:
#     occupied_beds = sorted(list(map(int, input().split())))
# except:
#     occupied_beds = []
#
#
# if len(occupied_beds) > 0:
#     mnO = occupied_beds[0]
#     mxO = occupied_beds[-1]
#
# mass_free_beds = [bed for bed in mass_beds if bed not in occupied_beds]
# mn = mass_free_beds[0]
# mx = mass_free_beds[-1]
#
# def max_difference():
#
#     if mn < occupied_beds[0]:
#         Mx = mn - occupied_beds[0]
#     if mx > occupied_beds[-1]:
#         Mx = max(mx, occupied_beds[-1])
#
#     for i in range(len(occupied_beds) - 1):
#         dif = occupied_beds[i + 1] - occupied_beds[i]
#         Mx = max(Mx, dif)
#
#     return Mx
#
# for i in range(n - k):
#     max_distanse_cats = max_difference() // 2
#     if mn - occupied_beds[0] >= max_distanse_cats * 2:
#         occupied_beds = sorted(occupied_beds.append(mn))
#         mass_free_beds.pop(mass_free_beds.index(mn))
#     if mx - occupied_beds[-1] >= max_distanse_cats * 2:
#         occupied_beds = sorted(occupied_beds.append(mx))
#         mass_free_beds.pop(mass_free_beds.index(mx))
#
#     flag = False
#     while not flag:
#         for i in range(len(occupied_beds) - 1):
#             dif = occupied_beds[i + 1] - occupied_beds[i]
#             if dif//2 >= max_distanse_cats:
#                 for x in range(dif - max_distanse_cats * 2):
#                     value = occupied_beds[i] + max_distanse_cats + x
#                     if value in mass_free_beds:
#                         occupied_beds = sorted(occupied_beds.append(value))
#                         mass_free_beds.pop(mass_free_beds.index(value))
#                         flag = True
#                         break
#                 if flag: break
#             if flag: break
#         max_distanse_cats -= 1
#     print('yes')
#
# print(occupied_beds, mass_free_beds)





# input_value = list(map(int, input().split()))
# n, m, k = input_value[0], input_value[1], input_value[2]
#
# mass_beds = sorted(list(map(int, input().split())))
# occupied_beds = list(map(int, input().split())) if k > 0 else []
# occupied_beds.append(-10 ** 100)
# occupied_beds.append(10 ** 100)
# occupied_beds.sort()



import random

n = random.randint(2, 10 ** 5)
m = random.randint(n, 10 ** 5)
k = random.randint(0, n)

mass_beds = set()
while len(mass_beds) != m:
    mass_beds.add(random.randint(1, 50))
mass_beds = list(mass_beds)
mass_beds.sort()

occupied_beds = []
while len(occupied_beds) != k:
    bed = mass_beds[random.randint(0, len(mass_beds) - 1)]
    if bed not in occupied_beds:
        occupied_beds.append(bed)
occupied_beds.append(-10 ** 10)
occupied_beds.append(10 ** 10)
occupied_beds.sort()

print(n, m, k)
print(mass_beds)
print(occupied_beds)

mass_free_beds = [bed for bed in mass_beds if bed not in occupied_beds]


for _ in range(n - k):
    memorable_bed = -1
    mx = -1
    for ind_ in range(len(occupied_beds) - 1):
        for ind, bed in enumerate(mass_free_beds):
            if bed > occupied_beds[ind_] and bed < occupied_beds[ind_ + 1]:
                mx_ = min(bed - occupied_beds[ind_], occupied_beds[ind_ + 1] - bed)
                if mx_ > mx:
                    mx = mx_
                    memorable_bed = bed

    occupied_beds.append(memorable_bed)
    occupied_beds.sort()
    # print(mass_free_beds, forgot_bed)
    mass_free_beds.remove(memorable_bed)

print()
print(occupied_beds)
print(min([occupied_beds[i + 1] - occupied_beds[i] for i in range(len(occupied_beds) - 1)]))

