# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[l-2]:
                nums[l]=nums[i]
                l+=1
        return l