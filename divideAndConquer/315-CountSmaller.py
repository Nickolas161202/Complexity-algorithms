
from typing import List, Tuple
class Solution: #time complexity: O(Nlog(N)); Space complexity: O(N)
    def mergeAndCount(self, left, right, res, index):
        nL = len(left)
        nR = len(right)
        merged = []
        inversions = 0
        j = 0
        i = j = 0
        while i < nL and j < nR: #effectively merges both arrays
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1 
            else:
                inversions += 1
                merged.append(right[j])
                j += 1
        #put all leftover elements from left or right  into the result array
        merged.extend(left[i:])
        while i < nR:
            merged.append(right[i])
            i +=1
            inversions +=1
        res[index] =  inversions
        return merged, inversions
    #main function 
    def reverse(self, S, res, index) -> Tuple[List[int], int]:
        n = len(S)
        #base Case: one element in S
        if n == 1:
            return S, 0
        mid = n // 2 
        A, countA = self.reverse(S[:mid], res, index) # recursively calls the function to the left side of the array
        B, countB = self.reverse(S[mid:], res, index)# recursively calls the function to the right side of the array
        print(A, B)
        M, cInv = self.mergeAndCount(A, B, res, index)

        return M, countA + countB + cInv #return merged array and the sum of inversions from left, right and left to right inversions
    
    #auxiliary function to LeetCode's enviroment.
    def reversePairs(self, nums: List[int]) -> int:
        res = [0  for i in range(len(nums))]
        self.reverse(nums, res, 0)
        return  res
    
#optional. Use it for testing
#arr =  ((input("Insert numbers separated by space: \n").split(" ")))
#arr =  [int(i) for i in arr ]
arr = [5,2,6,1]
sol = Solution().reversePairs(arr)
print("Here's the maximum sum of a Subarray from the inserted array:", sol)