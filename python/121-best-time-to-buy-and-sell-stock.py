class Solution:
    def maxProfit(prices: list[int]) -> int:
        """Brute force t=O(n^2), s=O(1)"""
        length = len(prices)
        profit = 0
        
        for buy in range(length):
            for sell in range(buy+1, length):
                # print(f'buy:{prices[buy]} sell:{prices[sell]}')
                profit = max(profit, prices[sell] - prices[buy])
        
        return profit

class Solution1:
    def maxProfit(prices: list[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit= prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            
            sell += 1

        return maxProfit

class Solution2:
    def maxProfit(prices: list[int]) -> int:
        buy = prices[0]
        sell = prices[0] - buy
        profit = sell - buy

        for p in prices[1:]:
            if (p - buy) > profit:
                profit = p - buy
            if p < buy:
                buy = p
        
        return profit



# test
tests = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([1,2], 1),
    ([], 0)
]

for prices, solution in tests:
    print(Solution1.maxProfit(prices) == solution)