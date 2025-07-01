class Solution: #solved using recursion and dynamic programming, although ther's a few ways more efficient
    def unique(self, m, n, dp):
        print(m, n, dp)
        if n == 0 or m == 0:
            return 1
        if dp[m][n] != -1:
            return dp[m][n]
        res =  self.unique(m-1, n, dp) + self.unique(m, n-1, dp)
        print("aaa", n, m)
        dp[m][n] = res
        return res        
    def uniquePaths(self, m: int, n: int) -> int:
        dp =  [[-1 for i in range(n)] for j in range(m)]
        res =  self.unique(m-1, n-1, dp)
        return res


print(Solution().uniquePaths(3, 2))