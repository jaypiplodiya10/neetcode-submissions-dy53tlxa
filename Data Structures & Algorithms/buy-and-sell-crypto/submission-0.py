class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,ans =0,1,0

        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
            else:
                ans = max(ans, prices[r]-prices[l])
            
            r+=1
        
        return ans
