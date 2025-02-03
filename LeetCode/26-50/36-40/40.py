from time import time

c = time()
class Solution:
    def combinationSum2(self, candidates: list[int], target: int):
        candidates.sort()

        def f(target, res, ind, candidates_, massive_flag):
            candidates_copy = candidates_[:]
            candidates_.insert(0, candidates[ind])
            if candidates_ not in massive_flag:
                massive_flag.append(candidates_[:])
                if target - candidates[ind] == 0:
                    res.append(candidates_[:])
                    candidates_ = candidates_copy
                    f(target, res, ind, candidates_, massive_flag)
                    return
                if target < 0 or ind - 1 < 0:
                    return
                f(target - candidates[ind], res, ind - 1, candidates_, massive_flag)
            else:
                i = 1
                while candidates[ind] == candidates[ind - i] and i <= ind:
                    i +=1
                if i > ind:
                    return
                ind -= i
            candidates_ = candidates_copy
            f(target, res, ind, candidates_, massive_flag)

        res = []
        f(target, res, len(candidates) - 1, [], [])
        return res

instance = Solution()
for i in range(300):
    res = instance.combinationSum2([3,1,3,5,1,1], 8)
print(res, time() - c)

class Solution:
    def combinationSum2(self, candidates: list[int], target: int):
        candidates.sort()
        res = []

        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res


instance = Solution()
c = time()
for i in range(300):
    res = instance.combinationSum2([3, 1, 3, 5, 1, 1], 8)
print(res, time() - c)
