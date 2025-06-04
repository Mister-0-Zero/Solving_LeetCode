class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        k = 0
        nums.append(-1000)

        while nums[k] != -1000:
            num = nums[k]

            while num == nums[k + 1]:
                nums.pop(k + 1)
            k += 1

        nums.remove(-1000)
        return k

instance = Solution()

nums = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 7, 7, 7, 8]
print(instance.removeDuplicates(nums))
print(nums)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        k = 0
        iter = 1

        while iter < len(nums):
            num = nums[k]

            while iter < len(nums) and num >= nums[iter]:
                iter += 1

            if not iter < len(nums): return k + 1

            nums[k + 1], nums[iter] = nums[iter], nums[k + 1]
            iter += 1
            k += 1

        return k + 1

instance = Solution()

nums = [1, 1]
print(instance.removeDuplicates(nums))
print(nums)