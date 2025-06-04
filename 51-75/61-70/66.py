class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        flag = 1
        for i in range(len(digits) - 1, -1, -1):
            new_val = digits[i] + 1
            digits[i] = new_val % 10
            if new_val < 10:
                flag = 0
                break
        if flag:
            return [1] + digits

instance = Solution()
mass = list(map(int, list("99999")))
print(mass)
res = instance.plusOne(mass)
print(res)