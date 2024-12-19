# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortNums=sorted(nums)
        d={}
        for i,num in enumerate(sortNums):
            if num not in d:
                d[num]=i
        res=[]
        for num in nums:
            res.append(d[num])
        return res
        