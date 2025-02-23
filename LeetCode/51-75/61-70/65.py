class Solution:
    def isNumber(self, s: str) -> bool:
        alf_valid = '0123456789.eE'
        if s[0] in "+-":
            s = s[1:]
        if s == ".":
            return False
        ind = 0
        while ind < len(s):
            print(ind)
            if s[ind] not in alf_valid:
                return False
            if s[ind] == ".":
                alf_valid = '0123456789eE'
            if s[ind] in "eE":
                alf_valid = "0123456789"
                if ind - 1 < 0:
                    return False
                if s[ind - 1] == ".":
                    if ind - 2 < 0:
                        return False
                if ind + 1 == len(s):
                    return False
                if s[ind + 1] in "-+":
                    if ind + 2 == len(s):
                        return False
                    ind += 1
            ind += 1
        return True

instance = Solution()
res = instance.isNumber("005047e+6")
print(res)
s = "+"
print(len(s) == 1 and s in ".-+eE")