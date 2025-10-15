# Best Time to Buy and Sell Stock II
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        sell_index = 1
        max_profit = 0
        profit = False

        while sell_index < len(prices):
            if prices[sell_index] > prices[sell_index - 1]:
                profit = True
            else:
                if profit:
                    max_profit += prices[sell_index-1] - prices[buy_index]
                    profit = False
                buy_index = sell_index
            
            sell_index += 1
            
        if profit:
            max_profit += prices[sell_index-1] - prices[buy_index]

        return max_profit

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    print(solution.maxProfit([1,2,3,4,5]))
    print(solution.maxProfit([7,6,4,3,1]))