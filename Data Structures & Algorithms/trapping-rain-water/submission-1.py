class Solution:
    def trap(self, height: List[int]) -> int:
        
        # two pointers
        # pointer at the beginning, pointer at the end
        if not height: return 0
        l, r = 0, len(height) - 1
        res = 0
        maxL, maxR = height[l], height[r]

        while l < r: 
            if maxL < maxR: 
                l += 1
                # max(0, 2)
                # maxL = 2
                # res = 2 - 2 = 0
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else: 
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res




