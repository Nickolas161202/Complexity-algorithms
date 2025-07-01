class Solution:
    dp  = dict()
    def tribonacci(self, n: int) -> int:
        if  n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n in Solution.dp:
            return Solution.dp[n]
        res =  self.tribonacci(n-3) + self.tribonacci(n-1) + self.tribonacci(n-2)
        Solution.dp[n] = res
        return res
    
