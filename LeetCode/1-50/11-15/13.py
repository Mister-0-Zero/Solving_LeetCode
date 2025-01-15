class Solution:
    def romanToInt(self, s: str) -> int:
        dig1 = {'M': 1000,  'D': 500,  'C': 100,
               'L': 50,  'X': 10, 'V': 5, 'I': 1}
        dig2 = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4,}
        res = 0
        for key, val in dig2.items():
            if key in s:
                s = s.replace(key, '')
                res += val
        for key, val in dig1.items():
            res += val * s.count(key)
        return res
