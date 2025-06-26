from typing import List

class Solution:
    dp =  dict()
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <2:
            return cost[0]
    

arr = [10,15,20]
print(Solution().minCostClimbingStairs(arr))