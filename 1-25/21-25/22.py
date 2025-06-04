class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(openP, closeP, s):
            if openP + closeP == n * 2:
                res.append(s)
                return

            if openP < n:
                dfs(openP + 1, closeP, s + "(")

            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")

        return res

instance = Solution()
print(instance.generateParenthesis(4))



