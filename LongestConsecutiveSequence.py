#https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums) #create a hashset with the array elements
        longest=0
        for n in nums: #check if the number is the start of a sequence(there is no number in the hashset one less than the number).
            if(n-1) not in numSet:
                length=0#initialize length variable which keeps track of the sequence.
                while(n+length) in numSet:
                    length+=1
                longest=max(length,longest)
        return longest


        