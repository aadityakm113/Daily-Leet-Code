#https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we use a two pointer approach and check the profit between the two days
        #if the profit is negative, shift the left pointer to the right pointer's position
        l=0
        r=1
        maxP=0 
        while r<len(prices):
            #profitable case
            if prices[l]<prices[r]: #eg l=1 r=7
                profit=prices[r]-prices[l]
                maxP=max(maxP,profit) #keep a track of the current maximum
            else:
                l=r #shift left pointer to the right position
            r+=1#increment the value of the right pointer
        return maxP
        