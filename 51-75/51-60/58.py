#без комментариев
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(" ")
        ind = len(s) - 1
        while ind >= 0 and s[ind] != " ":
            ind -= 1
        if ind < 0: return len(s)
        return len(s) - ind - 1

instance = Solution()
s = "sfd ss df sdfs  "
res = instance.lengthOfLastWord(s)
print(res)
