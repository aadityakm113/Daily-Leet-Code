# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialise a resultant array the size of the given array with default values of 0
        res=[0]*len(temperatures)
        # create a stack with a pair of values [temp,index]
        stack=[]
        for i,t in enumerate(temperatures):
            # stack must not be empty.
            # check if the temperature is greater than the top of the stack
            while stack and t>temperatures[stack[-1]]:
                index=stack.pop()
                res[index]=(i-index)
            stack.append(i)
        return res        