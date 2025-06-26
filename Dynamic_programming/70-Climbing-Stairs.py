class Solution:

    dp =  dict()
    def climb(self, n, arr):
        if arr[n-1] !=  -1:
            return arr[n-1]
        for i in range(n-2): 
            val = self.climb(n-1, arr) + self.climb(n-2, arr)
        arr[n-1] = val
        return val
    ## Faster Solution, but use more memory.
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        if n in Solution.dp:
            return Solution.dp[n]
        Solution.dp[n] =  self.climbStairs(n-1) + self.climbStairs(n-2)
        return Solution.dp[n]
    
    ''' A little bit slower solution, but uses less memory 
        def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        if n == 2:
            return 2
        dp = [-1 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        
        a = self.climb(n, dp)
        return a
    '''

    

print(Solution().climbStairs(4))