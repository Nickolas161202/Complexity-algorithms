from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        max_gas_cost_diff = 0
        gas_cost_diff = 0
        gas_station = 0
        n =  len(gas)
        for i in range(n):
            max_gas_cost_diff += gas[i] - cost[i]
            gas_cost_diff +=  gas[i] - cost[i]
            if gas_cost_diff < 0:
                gas_cost_diff = 0
                gas_station = i+1
        if max_gas_cost_diff < 0:
            gas_station = -1
        return gas_station
            

gas = [5,8,2,8]
cost = [6,5,6,6]
res =  Solution().canCompleteCircuit(gas, cost)
print(res)