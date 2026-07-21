class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        maxP = 0
        for i in range(1,len(prices)):
            if prices[i] > min:
                sell = prices[i] - min
                if sell > maxP:
                    maxP = sell
            else:
                min = prices[i]
        return maxP