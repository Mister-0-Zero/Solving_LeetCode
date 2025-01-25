class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        list_perm = permuitation(nums)
        list_perm.sort()
        for ind, perm in enumerate(list_perm):
            if perm == nums:
                if ind != len(list_perm) - 1:
                    nums[:] = list_perm[ind + 1]
                    return
                else:
                    nums[:] = list_perm[0]
                    return

def permuitation(massive, n = 0, res = None):
    if res is None:
        res = []

    if n == len(massive):
        res.append(massive[:])

        return res

    for i in range(n, len(massive)):
        massive[n], massive[i] = massive[i], massive[n]
        permuitation(massive, n + 1, res)
        massive[n], massive[i] = massive[i], massive[n]

    return res

mas = [1, 3, 2]
instance = Solution()
instance.nextPermutation(mas)

print(mas)

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:

        nums_ = {}
        remember = []
        flag = 0

        for ind in range(len(nums) - 1, -1, -1):
            num = nums[ind]

            for ind_, num_ in nums_.items():
                if num_ > num:
                    if remember:
                        if num_ <= remember[1]:
                            remember = [ind_, num_]
                    else:
                        remember = [ind_, num_]
                    flag = 1

            if flag:
                nums[ind], nums[remember[0]] = nums[remember[0]], nums[ind]
                nums[ind + 1:] = sorted(nums[ind + 1:])
                return nums

            nums_[ind] = num

        nums.sort()


mas = [1, 3, 2]

instance = Solution()
result = instance.nextPermutation(mas)
print(mas)



