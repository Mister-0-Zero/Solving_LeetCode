from random import randint
from time import time

# My decision
class Solution(object):
    def twoSum(self, nums: list[int], target: int, id_sol = 0):

        nums_is = nums
        nums = set(sorted(nums))
        nums_str = {str(num) for id,num in enumerate(nums)}

        flag = 1
        info=[]
        for id, num in enumerate(nums):

            new_target = target - num

            if str(new_target) in nums_str:
                for ind, num2 in enumerate(nums):

                    if num2 == new_target:
                        info=[num,num2]
                        flag = 0

                        # file.txt = open('find_sol.txt', 'w')
                        # file.txt.write('[')
                        # for i, num_ in enumerate(nums_str):
                        #     file.txt.write(num_ + ', ' )
                        # file.txt.write(']')


                        break

            if flag==0:
                break

        if len(info)==2:

            res=[]
            num=info[0]
            num2=info[1]
            for id, num3 in enumerate(nums_is):
                if num3 == num or num3==num2:
                    res.append(id)
                if len(res)==2:
                    return res

        return f'нет решений'

# brute force solution
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
# the proposed solution
class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = dict()  # pairs {value: index}

        for index, value in enumerate(nums):
            pairValue = target - value
            if pairValue in seen:
                return [seen[pairValue], index]
            seen[value] = index

#second the proposed solution
class Solution4:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = sorted((value, index) for index, value in enumerate(nums))
        l, r = 0, len(nums)-1

        while l < r:
            sm = nums[l][0] + nums[r][0]
            if sm > target:
                r -= 1
            elif sm < target:
                l +=1
            else:
                break

        return [nums[l][1], nums[r][1]]

b = Solution()
b2 = Solution2()
b3 = Solution3()
b4= Solution4()

for i in range(100):
    a = [randint(-10 ** 6, 10 ** 6) for _ in range(10 ** 4)]

    c = time()
    res = b.twoSum(a, 190)
    c1 = time() - c

    c = time()
    res2 = b2.twoSum(a,190)
    c2 = time() - c

    c = time()
    res3 = b3.twoSum(a, 190)
    c3 = time() - c

    c = time()
    res4 = b4.twoSum(a, 190)
    c4 = time() - c

    if len(res) == 2:
        print(c1,c2,c3,c4,sep='\n')
        break

print('Конец программы')