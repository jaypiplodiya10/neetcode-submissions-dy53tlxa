class Solution:
    def rec(self, n, idx, dp):
        if idx < 0: return 0
        if idx==0: return 1

        if dp[idx] != -1: return dp[idx]

        l = self.rec(n, idx-1, dp)
        r = self.rec(n, idx-2, dp)

        dp[idx] = l+r
        return dp[idx]

    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)

        dp[0]=1; dp[1]=1
        for idx in range(2, n+1):
            dp[idx] = dp[idx-1]+dp[idx-2]
        
        return dp[n]