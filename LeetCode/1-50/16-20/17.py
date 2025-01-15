class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dictionary = {"2": 'abc', "3": 'def', "4": 'ghi', "5": 'jkl', "6": 'mno', "7": 'pqrs', "8": 'tuv', "9": 'wxyz'}
        inp = list(digits)
        if not inp: return ""
        res = []
        for i in range(len(inp)):
            if not res:
                for j in dictionary[inp[0]]:
                    res.append(f"{j}")
                continue

            res_ = []
            for j in res:
                for k in dictionary[inp[i]]:
                    res_.append(j + k)
            res = res_.copy()
        return res

exempl = Solution()
print(exempl.letterCombinations("23"))
