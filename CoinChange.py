#https://leetcode.com/problems/coin-change/description/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1) #set default value to max and length of array to amount+1
        dp[0]=0 # base case 
        for a in range(1,amount+1): #iterating through the coins array
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a],1+dp[a-c]) #finds the dp value for each amount
        return dp[amount] if dp[amount]!=amount+1 else -1
        