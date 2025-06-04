class Solution:
    def mySqrt(self, x: int) -> int:
        number = x // 2
        while number * number > x:
            number //= 2
        top, down = (number + 1) * 2, number
        step = 1
        print(top, down)

        while step != 0:
            step = (top - down) // 2
            if (down + step) * (down + step) <= x:
                down += step
            else:
                top -= step
        return down

instance = Solution()
res = instance.mySqrt(121)
print(res, res ** 2)