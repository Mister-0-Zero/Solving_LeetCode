class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def f(subtarget, ind, condition, res):
            if subtarget == 0:
                res.append(condition[:])
                return
            if subtarget < 0 or ind < 0:
                return

            condition.append(candidates[ind])
            f(subtarget - candidates[ind], ind, condition, res)
            condition.pop()
            f(subtarget, ind - 1, condition, res)

        result = []
        f(target, len(candidates) - 1, [], result)
        return result


# Тест
instance = Solution()
res = instance.combinationSum([2, 3, 6, 7], 7)
print(res)
