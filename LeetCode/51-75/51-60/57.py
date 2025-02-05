class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        res = [newInterval]
        flag = 0 #может быть случай, несколько интервалов будут ниже исхордного, их надо будет
        # добавлять в начало массива, flag будет указывать на какое место вставлять
        for ind, value in enumerate(intervals):
            start, end = value
            if end < res[-1][0]: #проводим все возможные проверки, сначало смотрим на конец исследуемого интервала
                res.insert(flag, value)
                flag +=1
            elif end == res[-1][0]:
                res[-1][0] = start
            else: #если понимаем, что конец дальше начала интервала в res[-1], то смотрим как относительно начала он находится
                if start < res[-1][0]:
                    res[-1][0] = start
                    if end > res[-1][1]:
                        res[-1][1] = end
                elif start <= res[-1][1]:
                    if end > res[-1][1]:
                        res[-1][1] = end
                else:
                    res.append(value)

        return res

instance = Solution()
res = instance.insert([[2,6],[7,9]], [15,18])
print(res)

#данное решение выглядит попроще, но работает гораздо медленее, так как используется pop и сортировка занимающие много времени
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        intervals.append(newInterval)
        intervals.sort()
        ind = 0

        while ind < len(intervals) - 1:
            x_f, y_f = intervals[ind]
            x_s, y_s = intervals[ind + 1]
            if x_f <= x_s <= y_f:
                intervals[ind][1] = max(intervals[ind][1], y_s)
                intervals.pop(ind + 1)
            else:
                ind += 1

        return intervals

