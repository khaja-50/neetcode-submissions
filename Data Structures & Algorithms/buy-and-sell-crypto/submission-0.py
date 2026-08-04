class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        maximum=0
        for i in range(1,len(prices)):
            if prices[i]<minimum:
                minimum=prices[i]
            else:
                profit=prices[i]-minimum
                maximum=max(profit,maximum)
        return maximum

            

        