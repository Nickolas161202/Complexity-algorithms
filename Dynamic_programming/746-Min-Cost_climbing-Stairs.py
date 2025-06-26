from typing import List

class Solution:
    def __init__(self):
        self.dp = dict()

    def minCost(self, cost: List[int], n: int) -> int:
        if n < 0:
            return 0
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = cost[n] + min(self.minCost(cost, n - 1), self.minCost(cost, n - 2))
        return self.dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return min(self.minCost(cost, n - 1), self.minCost(cost, n - 2))

arr = [10, 15, 20]
print(Solution().minCostClimbingStairs(arr))