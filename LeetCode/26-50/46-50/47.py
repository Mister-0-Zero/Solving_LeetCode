class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def f(n, dictionary = {}, res = None):
            if res is None:
                res = []
            if n == len(nums):
                res.append(nums[:])
            for i in range(n, len(nums)):
                if nums[n] == nums[i] and n != i:
                    continue
                nums[n], nums[i] = nums[i], nums[n]
                if nums not in res: f(n + 1, dictionary,  res)
                nums[n], nums[i] = nums[i], nums[n]
            return res

        return f(0)


# Тест
instance = Solution()
res = instance.permuteUnique([1, 1, 2, 2])
print(res)


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for n in dMap:
                if dMap[n] > 0:
                    cur.append(n)
                    dMap[n] -= 1
                    dfs(cur)
                    cur.pop()
                    dMap[n] += 1

        dMap = {}
        res = []
        for n in nums:
            dMap[n] = dMap.get(n, 0) + 1
        dfs([])
        return res

instance = Solution()
res = instance.permuteUnique([1, 1, 2, 2])
print(res)