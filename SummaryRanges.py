# https://leetcode.com/problems/summary-ranges
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        i = 0
        while i < len(nums):
            start = nums[i]
            # Traverse the consecutive sequence
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            # Check if it's a range or a single number
            if start != nums[i]:
                out.append(f"{start}->{nums[i]}")
            else:
                out.append(str(start))
            
            # Move to the next number
            i += 1
        return out
