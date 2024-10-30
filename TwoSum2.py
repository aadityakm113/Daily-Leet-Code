# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    # HashMap
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map={}
        out=[]
        for i in range(len(numbers)):
            x=target-numbers[i]
            if x in map:
                return [map[x]+1,i+1]
            else: 
                map[numbers[i]]=i
        return out
    
    # Two Pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r-=1
            elif numbers[l]+numbers[r]<target:
                l+=1
         