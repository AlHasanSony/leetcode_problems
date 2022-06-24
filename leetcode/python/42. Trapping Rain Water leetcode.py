
#problem link -  https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height [left], height [right]
        result = 0
        
        while left < right: #while left is less than right
            if leftMax < rightMax: #if leftMax is less than rightMax
                left += 1 #increment left
                leftMax = max(leftMax, height[left]) #update leftMax
                result += leftMax - height[left] #update result
            else: #else
                right -=1 #decrement right
                rightMax = max(rightMax, height[right]) #update rightMax
                result += rightMax - height[right] #update result
                
        return result
        
        