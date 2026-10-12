class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        min_price = prices[0]
        for p in prices:
            ans = max(ans, p - min_price)
            min_price = min(min_price, p)
        return ans


# 根据本次对话中的写法整理；题目保证 prices 非空。
