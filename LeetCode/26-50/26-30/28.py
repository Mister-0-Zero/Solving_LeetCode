class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle in haystack: return haystack.index(needle)
        # return -1

        for i in range(len(haystack) - len(needle) + 1):
            flag = 1
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    flag = 0
                    break
            if flag:
                return i
        return -1

instance = Solution()
print(instance.strStr("a", "a"))