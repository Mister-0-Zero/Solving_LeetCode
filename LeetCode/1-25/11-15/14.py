class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_s = min(strs, key=lambda s: len(s))
        l_ms = len(min_s)
        pres = 1
        while True:
            for i in range(pres):
                if all(min_s[i:l_ms] in str_ for str_ in strs): return min_s[i:l_ms]
            l_ms -= 1
            pres += 1
            if l_ms == 1:  return ''



ex = Solution()
print(ex.longestCommonPrefix(["flower", "flow", "flight"]))