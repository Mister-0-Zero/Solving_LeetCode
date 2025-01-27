class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return 1 if target > nums[0] else 0

        right = len(nums) - 1
        left = 0

        def search_f(left, right):

            index = (right + left) // 2
            while right >= left:
                if target < nums[index]:
                    right = index - 1
                    return search_f(left, right)
                elif target > nums[index]:
                    left = index + 1
                    return search_f(left, right)

                else:
                    return index
            if right == -1:
                return 0
            if nums[right] > target:
                return right
            else:
                return right + 1

        res = search_f(left, right)

        return res