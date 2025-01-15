class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = ''
        mx = 0
        for sim in s:
            if sim not in k:
                k += sim
            else:
                if mx < len(k):
                    mx = len(k)
                k = k[k.index(sim):] + sim
        if mx < len(k): mx = len(k)
        return mx

import string
from random import *

alf = string.ascii_letters + "12344567890"
leng = randint(20, 21)
len_alf = len(alf) - 1
s = ''
for i in range(leng):
    s += alf[randint(0, len_alf)]
print(s)
ex = Solution()
res = ex.lengthOfLongestSubstring(s)
print(res)