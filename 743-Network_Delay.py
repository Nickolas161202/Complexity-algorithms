import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d =  [10**9 for i in range(n)]
        for x in times:
            x[0] =  x[0] -1
            x[1] = x[1] -1
        k =  k-1
        d[k] = 0
        heap = []
        heapq.heappush(heap, [0, k]) # [distance, node]
        while len(heap) != 0:
            distU, nodeU =  heapq.heappop(heap)
            for x in times:
                if nodeU ==  x[0]:
                    node_v =  x[1]
                    weight_v =  x[2]
                    if d[node_v] >  distU + weight_v:
                        d[node_v] =  distU + weight_v
                        heapq.heappush(heap, [d[node_v], node_v])
        res =  max(d)
        if res == 10**9:
            res = -1
        return res
times =  [[2,1,1],[2,3,1],[3,4,1]]
n =  4
k = 2
print(Solution().networkDelayTime(times, n, k))
