class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1: return [strs]
        dict_ = {}
        for str in strs:
            dict_sim = {}
            for sim in str:
                dict_sim[ord(sim)] = 0
            for sim in str:
                dict_sim[ord(sim)] += 1

            keys = list(dict_sim.keys())
            keys.sort()
            code = ""

            for key in keys:
                code += f"{key}:{dict_sim[key]}"

            if code in dict_:
                dict_[code].append(str)
            else:
                dict_[code] = [str]

        res = []
        for value in dict_.values():
            res.append(value)

        return res

instance = Solution()
mass = ["pit", "pet", "tip"]
res = instance.groupAnagrams(mass)
print(res)


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1: return [strs]

        const = ord("a")
        dict_ = {}
        for str in strs:
            alf = [0] * 26

            for sim in str:
                alf[ord(sim) - const] += 1

            code = tuple(alf)

            if code in dict_:
                dict_[code].append(str)
            else:
                dict_[code] = [str]

        res = []
        for value in dict_.values():
            res.append(value)

        return res

instance = Solution()
mass = ["pit", "pet", "tip"]
res = instance.groupAnagrams(mass)
print(res)

