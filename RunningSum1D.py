# https://leetcode.com/problems/running-sum-of-1d-array/description/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        runningSum=0
        for i in range(len(nums)):
            runningSum+=nums[i]
            res.append(runningSum)
        return res