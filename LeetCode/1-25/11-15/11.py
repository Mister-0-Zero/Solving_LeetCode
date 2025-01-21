class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            val_l, val_r = height[left], height[right]
            max_area = max(max_area, (right - left) * min(val_l, val_r))

            if  val_l < val_r:
                left += 1
            else:
                right -= 1

        return max_area