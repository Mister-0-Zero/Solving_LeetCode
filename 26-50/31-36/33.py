class Solution:
    def search(self, nums: list[int], target: int) -> int:

        if len(nums) == 1:
            return -1 if target != nums[0] else 0

        length = len(nums) - 1

        flag = 1

        mass_ind = [0, length // 4, length * 2 // 4, length * 3 // 4, length]
        index_minus, index_plus = 0, len(nums) - 1
        index = (index_plus + index_minus) // 2

        while flag:
            flag = 0
            for i in range(5 - 1):
                if nums[mass_ind[i]] > nums[mass_ind[i + 1]]:
                    if mass_ind[i + 1] - mass_ind[i] == 1:
                        if target < nums[0]:
                            index_minus, index_plus = mass_ind[i + 1], len(nums) - 1
                        else:
                            index_minus, index_plus = 0, mass_ind[i]

                        index = (index_plus + index_minus) // 2

                        flag = 0
                        break

                    length = mass_ind[i + 1] - mass_ind[i]
                    mass_ind = [mass_ind[i],
                                length // 4 + mass_ind[i],
                                length * 2 // 4 + mass_ind[i],
                                length * 3 // 4 + mass_ind[i],
                                mass_ind[i + 1]]
                    flag = 1


        def function(index_minus, index, index_plus):
            while index_minus <= index_plus:
                if nums[index] < target:
                    index_minus = index + 1
                elif nums[index] > target:
                    index_plus = index - 1
                else:
                    return index
                index = (index_plus + index_minus) // 2
            return -1

        res = function(index_minus, index, index_plus)

        return res


instance = Solution()
res = instance.search([1, 3], 3)
print(res)