class Solution:
    def longestPalindrome(self, s: str) -> str:
        x = 1
        abs_str = s
        len_st = len(s)
        while len_st >= x + 1:
            for i in range(x):
                s = abs_str[i: len_st - x + i + 1]
                len_s = len(s)
                if len(s) % 2 == 0:
                    if s[:len_s // 2][::-1] == s[len_s // 2:]:
                        return s
                else:
                    if s[:len_s // 2][::-1] == s[len_s // 2 + 1:]:
                        return s
            x += 1
        return abs_str[0]


def f():
    s = 'saasaaf'
    ex = Solution()
    res = ex.longestPalindrome(s)
    print(res)

f()