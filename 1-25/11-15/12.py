class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        while num >= 1000:
            num -= 1000
            res += "M"
        if num >=900:
            num -= 900
            res += 'CM'
        if num >= 500:
            num -= 500
            res += 'D'
        if num >= 400:
            num -= 400
            res += 'CD'
        while num >=100:
            num -= 100
            res += 'C'
        if num >= 90:
            num -= 90
            res += 'XC'
        if num >= 50:
            num -= 50
            res += 'L'
        if num >= 40:
            num -= 40
            res += 'XL'
        while num >=10:
            num -= 10
            res +='X'
        if num == 9:
            num -= 9
            res += 'IX'
        if num >= 5:
            num -= 5
            res += 'V'
        if num == 4:
            num -= 4
            res += 'IV'
        while num > 0:
            num -= 1
            res += 'I'
        return res

class Solution:
    def intToRoman(self, num: int) -> str:
        dig = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
               90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        val = list(dig.keys())
        print(val)
        res = ''
        ind = 0
        while num > 0:
            current_val = val[ind]
            while num - current_val > -1:
                num -= current_val
                res += dig[current_val]
            ind += 1

            if num == 0: return res

ex = Solution()
print(ex.intToRoman(4030))