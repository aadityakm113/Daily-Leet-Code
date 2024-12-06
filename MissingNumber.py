# https://leetcode.com/problems/missing-number/
#O(n^2)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
#O(n)
#find the difference between the expected sum and the sum of numbers in the array
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1))-sum(nums)