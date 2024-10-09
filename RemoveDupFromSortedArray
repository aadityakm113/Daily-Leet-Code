#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #use two pointers l and r.
        #l starts from 1 as the ith index value is unique
        #compare the right pointer with the previous value to see if it a new number or not
        #if it is a new number, shift that number to position l and increment l
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]: #new number found
                nums[l]=nums[r] #shift new number to l
                l+=1
        return l