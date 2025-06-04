from random import randint

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        for ind1, n1 in enumerate(num1[::-1]):
            for ind2, n2 in enumerate(num2[::-1]):
                mul = int(n2) * int(n1)
                pos, pos1 = ind1 + ind2, ind1 + ind2 + 1

                res[pos] += mul % 10
                res[pos1] += mul // 10

                if res[pos] >= 10:
                    res[pos1] += res[pos] // 10
                    res[pos] %= 10

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return ''.join(map(str, res[::-1]))


instance = Solution()
num1 = str(randint(1, 200))
num2 = str(randint(1, 200))
print(f"{num1} * {num2} = {instance.multiply(num1, num2)}")




instance = Solution()
# for _ in range(1000):
#     num1 = str(randint(1, 9999))
#     num2 = str(randint(1, 9999))
#     res = instance.multiply(num1, num2)
#     flag = res == str(int(num1) * int(num2))
#     print(res == str(int(num1) * int(num2)), res, str(int(num1) * int(num2)))
#     print()
#     if not flag: break
res = instance.multiply("17849419788197", "877968504004372811")
print(res)
print(17849419788197 * 877968504004372811)

