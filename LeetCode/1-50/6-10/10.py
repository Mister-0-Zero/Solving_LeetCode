class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = p.replace(' ','')
        p = list(p)
        for ind, sim in enumerate(s):
            flag = 1
            try:
                if sim != p[ind]:
                    if p[ind] != '.':
                        if p[ind] == '*':
                            try:
                                if p[ind + 1] == sim:
                                    p.pop(ind)
                                    flag = 0
                            except:
                                pass

                            if flag:
                                p[ind] = sim
                                p.insert(ind + 1, '*')
                    else:
                        p[ind] = sim
            except:
                return False
        if s in ''.join(p):
            return True
        else:
            return False

# p = 'c * a * b'
# s = 'ab'
#
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         p = list(p.replace(' ', ''))
#         s = list(s)
#         for ind, sim in enumerate(p):
#             if sim == s[0] or sim == '.' or sim == '*':
#                 p = p[ind:]
#                 break
#         for ind, sim in enumerate(s):
#             if p[ind] != '.' or p[ind] != '*' or p[ind] != sim:
#                 return False
#             if p[ind] == '*':
#                 try:
#                     p[ind + 1]
#                 except:
#                     return True
#                 try:
#                     if p[ind + 1] != s[ind + 1]:
#                         p.insert(ind + 1, '*')







ex = Solution()
print(ex.isMatch('aa', "c*a*b"))