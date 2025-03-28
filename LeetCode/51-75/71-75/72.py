class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    # dp[i][j] := min # Of operations to convert word1[0..i) to word2[0..j)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
      dp[i][0] = i

    for j in range(1, n + 1):
      dp[0][j] = j

    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]

instance = Solution()
res = instance.minDistance("aasdfd", "asdf")
print(res)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        cache = {}
        def dfs(word1, word2, i, j):
            if i<0: #This means word1 is exhausted and word2 is at some j say 2, so to convert and empty string to string of length 3(since j at 2), 3 opertaions(insert) are needed i.e. j+1
                return j+1
            if j<0: #This means word2 is exhausted and word1 is at some i say 2, so to convert to empty string to string , 3 opertaions(delete) are needed i.e. i+1
                return i+1
            if (i,j) in cache:
                return cache[(i,j)]
            if word1[i] == word2[j]:
                cache[(i,j)] = dfs(word1, word2, i-1, j-1)
            else:
                cache[(i,j)] = min(1 + dfs(word1, word2, i, j-1), #Insert operation, hypothetical same char as word[j] is inserted to i+1, so now, i+1 and j matches so decrease only j.
                1 + dfs(word1, word2, i-1, j-1), #Replace operation, char at word[i] is replace with char at word[j] so both matches sop both are decreased.
                1 + dfs(word1, word2, i-1, j))#Delete operation, char at word[i] is deleted so i decreases.
            return cache[(i,j)]
        return dfs(word1, word2, n-1, m-1)