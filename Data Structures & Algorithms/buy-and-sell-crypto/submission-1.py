class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [0]*len(prices)
        min = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > min:
                arr[i]= prices[i]-min
            else:
                min = prices[i]
        return max(arr)