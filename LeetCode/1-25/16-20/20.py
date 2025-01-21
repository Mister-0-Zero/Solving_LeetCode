class Solution:
    def isValid(self, s: str) -> bool:
        if s.count("{") != s.count("}") or s.count("[") != s.count("]") or s.count("(") != s.count(")"): return False
        for ind in range(len(s)):
            print(s[ind])
            s_= s[ind:]
            if s[ind] in "{[(":
                try:
                    if s[ind] == "(":
                        prov = s_[: s_.index(")")]
                        if prov.count("{") != prov.count("}") or prov.count("[") != prov.count("]"): return False
                    if s[ind] == "[":
                        prov = s_[: s_.index("]")]
                        if prov.count("{") != prov.count("}") or prov.count("(") != prov.count(")"): return False
                    if s[ind] == "{":
                        prov = s_[: s_.index("}")]
                        if prov.count("(") != prov.count(")") or prov.count("[") != prov.count("]"): return False
                except:
                    return False
        return True


ex = Solution()
print(ex.isValid("{[}]"))

class Solution:
    def isValid(self, s: str) -> bool:
        if s.count("{") != s.count("}") or s.count("[") != s.count("]") or s.count("(") != s.count(")"): return False
        brek = []
        for sim in s:
            if sim in "({[":
                brek.append(sim)
            else:
                if brek:
                    if  sim == ")" and brek[-1] != "(" or \
                        sim == "}" and brek[-1] != "{" or \
                        sim == "]" and brek[-1] != "[": return False
                    else: brek = brek[:-1]
                else: return False
        return not brek

ex = Solution()
print(ex.isValid("{[}]"))
