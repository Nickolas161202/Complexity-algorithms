from typing import List

class Solution:
    def cross(self, arr, mid, left, right) -> int:
        sum = 0
        i =  mid
        leftSum =  float('-inf') #initialize left and right subarray sum
        rightSum =  float('-inf')
        
        while i >= left: #calculate the maximum subarray from mid to left
            sum   +=  arr[i]
            leftSum =  max(sum, leftSum) 
            i -= 1
        sum = 0

        for i in range(mid+1, right+1): #calculate the maximum array from mid to right
            sum += arr[i]
            rightSum =  max(rightSum, sum)
            
        return leftSum + rightSum
    
    # Main recursive function using divide and conquer to find max subarray sum
    def maxSub(self, arr,left, right) -> int: 
        #base case:when the array has only one element
        if left == right:
            return arr[left]

        mid = (left + right) // 2 #divide the array by 2

        #call the recursion to the left and right side in order to find the max subarray sum
        res1 = self.maxSub(arr, left, mid) 
        res2 = self.maxSub(arr, mid + 1, right)
        # find the max subarray sum that crosses the middle
        crossSum = self.cross( arr, mid, left, right) 

        return max(res1, res2, crossSum) #return the maximum of the three values

    #call function used by LeetCode 
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1 
        return self.maxSub(nums, left, right)

#Optional code to use outside Leetcode's enviroment
arr =  ((input("Insert numbers separated by space: \n").split(" ")))
arr =  [int(i) for i in arr ]
sol = Solution().maxSubArray(arr)
print("Here's the maximum sum of a Subarray from the inserted array:", sol)
