# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# User a set to keep track of all the numbers that are in the array and iterate from 1 to n and see if i is in the set or not
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        numSet=set(nums)
        for i in range(1,len(nums)+1):
            if i not in numSet:
                res.append(i)
        return res