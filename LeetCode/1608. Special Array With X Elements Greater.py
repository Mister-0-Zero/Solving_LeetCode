import random
import time

class Solution:
    def specialArray(self, nums: list[int]) -> int:

        nums.sort()
        mx = max(nums)
        lenght = len(nums)
        a_d = {nums[0]: 1}
        flag = nums[0]

        for i in range(1, lenght):
            num = nums[i]
            if num != flag:
                a_d[num] = 1
                flag = num
            else:
                a_d[num] += 1

        i = 0
        while i <= mx:

            if i == lenght:
                return i
            elif i > lenght:
                return -1
            elif i in a_d:
                lenght -= a_d[i]

            i += 1

        return -1

lenght = 10000
massive = [random.randint(0, 10000) for i in range(lenght)]
exepl = Solution()
res_time_mas = []
for i in range(30):
    c = time.time()
    res = exepl.specialArray(massive)
    res_time_mas.append( time.time() - c)

print(massive)
print(res)
print(sum(res_time_mas)/len(res_time_mas))
#0.006430403391520182
#0.00026051998138427735