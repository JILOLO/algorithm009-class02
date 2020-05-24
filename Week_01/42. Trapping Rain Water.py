class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        left, right = 0, len(height)-1
        max_left = max_right = 0
        res = 0
        while left < right:
            if height[left] <= height[right]:
                max_left = max(max_left, height[left])
                res += (max_left - height[left])
                left += 1
            elif height[left] > height[right]:
                max_right = max(max_right, height[right])
                res += (max_right - height[right])
                right -= 1
                
        return res