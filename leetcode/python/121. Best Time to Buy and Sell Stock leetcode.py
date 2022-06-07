#problem link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0 
        #initialize the max profit
        min_buy= (float('inf')) 
        #initialize the minimum buy price
        for price in prices: 
            #loop to get the prices
            min_buy=min(min_buy,price) 
            #update the minimum buy price
            max_profit=max(max_profit,price-min_buy) 
            #update the max profit
        return max_profit 
    #return the max profit