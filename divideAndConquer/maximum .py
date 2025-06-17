from typing import List

class Solution:
    def cross(self, arr, mid, left, right):
        sum = 0
        i =  mid
        leftSum =  float('-inf')
        rightSum =  float('-inf')
        while i >= left:
            sum   +=  arr[i]
            leftSum =  max(sum, leftSum) 
            i -= 1
        sum = 0
        for i in range(mid+1, right+1):
            sum += arr[i]
            rightSum =  max(rightSum, sum)
        return leftSum + rightSum
    def maxSub(self, arr,left, right):
        if left == right:
            return arr[left]

        mid = (left + right) // 2

        res1 = self.maxSub(arr, left, mid)
        res2 = self.maxSub(arr, mid + 1, right)
        crossSum = self.cross( arr, mid, left, right)
        return max(res1, res2, crossSum)

    
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1 
        return self.maxSub(nums, left, right)
