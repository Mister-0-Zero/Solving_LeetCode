class Solution:
    def jump(self, nums: list[int]) -> int:

        if len(nums) <= 1: return 0

        res = 0
        max_iteration = max(nums)
        current, remember_ind= len(nums) - 1, len(nums) - 1

        while remember_ind > 0:
            res += 1
            flag = remember_ind
            current = remember_ind
            for current in range(current - 1, current - max_iteration - 1\
                    if current - max_iteration - 1 > -2 else -1, -1):
                # print([current, nums[current]])
                if nums[current] + current >= flag:
                    remember_ind = current
            # print()

        return res

instance = Solution()
res = instance.jump([1,2,3,4,5])
print(res)