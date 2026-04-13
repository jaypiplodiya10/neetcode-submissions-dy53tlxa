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
        ans = 0

        prev1=1; prev2=1
        for idx in range(2, n+1):
            ans = prev2 + prev1
            prev1, prev2 = ans, prev1
        if n >=2:
            return ans
        else:
            return 1