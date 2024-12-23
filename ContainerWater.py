# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        while l<r:
            area=min(height[l],height[r])*(r-l)
            res=max(area,res)
            if height[l]<height[r]:
                l+=1
            # elif height[r]<height[l]:
            #     r-=1
            else:
                r-=1
        return res
        