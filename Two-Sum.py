#https://leetcode.com/problems/two-sum/description/
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
   def twoSum(self, nums: list[int], target: int) -> list[int]:
       for i in range (0,len(nums)):
           x=nums[i]
           y=target-x
           for j in range(0,len(nums)):
               if nums[j]==y:
                   if i==j:
                       j+=1
                   else:
                       out=[]
                       out.append(i)
                       out.append(j)
                       return out
               else:
                   j+=1
           i+=1
