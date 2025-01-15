class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        leng = len(nums1)
        ind = leng // 2

        if leng % 2 == 1:
            return float(nums1[ind])
        else:
            return (nums1[ind - 1] + nums1[ind]) / 2.0


ex = Solution()
res = ex.findMedianSortedArrays([1, 9], [5, 6])
print(res)  # Ожидаемый результат: 5.5
