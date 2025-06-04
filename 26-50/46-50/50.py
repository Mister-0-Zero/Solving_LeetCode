import time
import random

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1

        res = x
        kol_r = 0

        while 0 < abs(res) * 10 ** kol_r  < 1:
            kol_r += 1

        if x > 0 and kol_r * n > 100: return 0

        for _ in range(abs(n) - 1):
            res *= x

        return res if n > 0 else 1 / res

instance = Solution()
# while True:
#     x = random.randint(1, 1000)/100
#     n = random.randint(1, 10)
#     res = instance.myPow(x, n)
#     print(x, n)
#     print(res, x ** n)
#     print()
#     time.sleep(2)

x, n = -1.00000001, 15723521
c = time.time()
res = instance.myPow(x, n)
print(res, x ** n, res == x ** n)
print(time.time() - c)
print()

import time
import random

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1 or x == -1 and n % 2 == 0: return 1
        if x == -1 and n % 2 == 1: return -1

        flag = -1 if n < 0 else 1
        n = abs(n)
        mass = [x]
        cur_n = 2

        while cur_n <= n:
            mass.append(mass[-1] * mass[-1])
            cur_n *= 2
        cur_n //= 2

        res = mass[-1]
        ind = len(mass) - 2

        while cur_n != n:
            cur_plus = self.step(ind)
            if cur_n + cur_plus <= n:
                res *= mass[ind]
                cur_n += cur_plus
            ind -= 1

        return res if flag > 0 else 1 / res

    def step(self, ind):
        if ind == 0: return 1
        step = 2
        for _ in range(ind - 1):
            step *= 2
        return step

instance = Solution()
# while True:
#     x = random.randint(1, 1000)/100
#     n = random.randint(1, 10)
#     res = instance.myPow(x, n)
#     print(x, n)
#     print(res, x ** n)
#     print()
#     time.sleep(2)

c = time.time()
res = instance.myPow(x, n)
print(res, x ** n, res == x ** n)
print(time.time() - c)
print()

