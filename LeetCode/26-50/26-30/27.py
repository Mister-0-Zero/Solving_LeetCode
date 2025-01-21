class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        k = 0
        i = 0

        while i < len(nums):
            while i < len(nums) and nums[i] == val:
                i += 1
            if not i < len(nums): break
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
            i += 1

        return k


instance = Solution()
mass = [3, 2, 2, 3, 4]
print(instance.removeElement(mass, 3))
print(mass)


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Индекс для следующего элемента, который не равен val

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

instance = Solution()
mass = [3, 2, 2, 3, 4]
print(instance.removeElement(mass, 3))
print(mass)