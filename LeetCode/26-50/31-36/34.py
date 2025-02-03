class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        left = 0
        right = len(nums) - 1

        def find_f(left, right):

            index = (right + left) // 2

            while right >= left:

                if nums[index] > target:
                    right = index - 1
                    return find_f(left, right)
                elif nums[index] < target:
                    left = index + 1
                    return find_f(left, right)
                else:
                    index_ = index
                    while nums[index] == target and index > 0:
                        index -= 1
                    index = 0 if index == 0 and nums[index] == target else index + 1
                    while nums[index_] == target and index_ < len(nums) - 1:
                        index_ += 1
                    index_ = len(nums) - 1 if index_ == (len(nums) - 1) and nums[index_] == target else index_ - 1

                    return [index, index_]

            return [-1, -1]

        return find_f(left, right)



instance = Solution()
res = instance.searchRange([1, 4], 4)
print(res)
