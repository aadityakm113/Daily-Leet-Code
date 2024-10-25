# https://leetcode.com/problems/jump-game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if(i+nums[i]>=goal):
                goal=i #shift goal to i'th position
        return goal==0 #two possibilities at the end. goal=0 meaning the goal can be reached or goal!=0 meaning the goal cant be reached.