class Solution:
    def rec(self, m, n,dp):
        if m <0 or n<0: return 0
        if m==0 and n==0: return 1
        
        if dp[m][n] != -1: return dp[m][n]
        up = self.rec(m-1, n, dp)
        left = self.rec(m, n-1, dp)

        dp[m][n] = up+left
        return dp[m][n]

    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0]*(n+1) for _ in range(m+1)]
        dp[m-1][n-1]=1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                up = dp[i+1][j]
                left = dp[i][j+1]

                dp[i][j] += up+left
            
        return dp[0][0]
