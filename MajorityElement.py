# https://leetcode.com/problems/majority-element
# Using HashMap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        res,maxCount=0,0
        for n in nums:
            map[n]=1+map.get(n,0)
            res=n if map[n]>maxCount else res
            maxCount=max(map[n],maxCount)
        return res
    
# Boyer Moore
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count=0,0
        for n in nums:
            if count==0:
                res=n
            count+=(1 if n==res else -1)
        return res