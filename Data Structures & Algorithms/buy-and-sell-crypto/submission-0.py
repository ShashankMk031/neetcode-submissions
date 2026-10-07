class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_p = 0 
        price = float("inf")
        for val in prices: 
            if val < price: 
                price = val 
            profit = val - price 
            mx_p = max(profit, mx_p) 
        return mx_p 