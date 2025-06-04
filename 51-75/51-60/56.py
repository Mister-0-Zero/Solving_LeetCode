from random import randint
#представляю аж 3 решения задачи (ладно, ладно второе модификация 1, хотя можно так сказать и про 3)

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        #просто проходим по всем интервалам и объединяем если они пересекаются
        for x, y in intervals:
            flag = 1
            for ind, value in enumerate(res):
                x_, y_ = value[0], value[1]
                if x_ <= x <= y_:
                    if y > y_:
                        res[ind][1] = y
                        flag = 0
                        break
                    flag = 0
                if x_ <= y <= y_:
                    if x < x_:
                        res[ind][0] = x
                        flag = 0
                        break
                    flag = 0
            if flag:
                res.append([x, y])

        #а теперь объединяем если случай по типу: [[5, 8], [0, 7]]
        res.sort()
        ind = 0
        while ind < len(res) - 1:
            x_f, y_f = res[ind][0], res[ind][1]
            x_s, y_s = res[ind + 1][0], res[ind + 1][1]
            if x_f <= x_s <= y_f:
                if y_s > y_f:
                    res[ind][1] = y_s
                res.pop(ind + 1)
            else: ind += 1

        return res #квадратичная сложность, плохое решение

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        #тут мне пришло, что можно изначально отсортировать, тогда нужна будет лишь одна проверка в основном цикле
        #и не надо будет в конце делать доп действия по объединению
        intervals.sort()
        for x, y in intervals:
            flag = 1
            for ind, value in enumerate(res):
                x_, y_ = value[0], value[1]
                if x_ <= x <= y_:
                    if y > y_:
                        res[ind][1] = y
                        flag = 0
                        break
                    flag = 0
            if flag:
                res.append([x, y])

        return res

#ну а вот и эталон, все максимально просто, сортируем и идем один раз сравнивая с последним интервалом в res
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        intervals.sort()  # Сортируем по первому элементу
        res = [intervals[0]]  # Первый интервал добавляем в результат

        for x, y in intervals[1:]:  # Идём по оставшимся
            last_x, last_y = res[-1]  # Последний интервал в `res`

            if last_y >= x:  # Есть пересечение?
                res[-1][1] = max(last_y, y)  # Обновляем конец интервала
            else:
                res.append([x, y])  # Добавляем новый интервал

        return res

instance = Solution()
while True:
    mass_int = []
    i = 0
    while len(mass_int) < 5:
        x = randint(0 + i * 5, 10 + i * 5)
        y = randint(0 + i * 5, 10 + i * 5)
        if y < x:
            continue
        mass_int.append([x, y])
        i += 1
    print(mass_int)
    res = instance.merge([[1,10],[4,5],[6,7],[8,9]])
    print(res)
    print()
    vvod = input()
    if vvod: break
