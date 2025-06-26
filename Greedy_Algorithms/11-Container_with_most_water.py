from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_area = 0
        while left < right:
            if height[left] > height[right]:
                area = height[right] * (right - left)
                right -= 1
            else:
                area = height[left] * (right - left)
                left += 1
            if area > max_area:
               max_area =  area
        
    
        return max_area
                
#area =  altura_do_delimitador  * (distancia entre  left e right)

arr = [1,8,6,2,5,4,8,3,7]

Solution().maxArea(arr)

