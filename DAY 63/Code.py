class Solution(object):
    def maxProfit(self, prices):
        m = res = 0
        for x in reversed(prices):
            m = max(m,x)
            res = max(res,m-x)
        return res
