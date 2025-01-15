class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        difference = float('inf')

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                difference_ = abs(target - total)

                if difference_ < difference:
                    difference = difference_
                    res = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total

        return res
