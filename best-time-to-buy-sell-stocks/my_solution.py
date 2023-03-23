class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Track Current Max
        maxProfit = 0
        # Track sell and buy pointers (l is buy, r is sell)
        l = 0
        r = 1 # stagger the right

        # while r is in bounds of prices 
        while r < len(prices):

            # If sell date - buy date is higher than the maxProfit
            if prices[r] - prices[l] > maxProfit:
                maxProfit = prices[r] - prices[l]
            
            # iterate buy date to the lowest price
            if prices[r] < prices[l]:
                l = r
            
            # Iterate right regardless (buy and sell can't be on the same day)
            r += 1
        
        return maxProfit