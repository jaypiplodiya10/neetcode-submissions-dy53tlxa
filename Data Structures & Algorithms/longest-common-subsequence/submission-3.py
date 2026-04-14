class Solution:
    def rec(self, txt1, txt2, idx1, idx2, dp):
        if idx1 < 0 or idx2 < 0 : return 0

        if dp[idx1][idx2] != -1: return dp[idx1][idx2]
        take = self.rec(txt1, txt2, idx1-1, idx2-1, dp)+1 if txt1[idx1]==txt2[idx2] else 0
        not_take = max(self.rec(txt1, txt2, idx1-1, idx2, dp), self.rec(txt1, txt2, idx1, idx2-1, dp))

        dp[idx1][idx2]= max(take, not_take)
        return dp[idx1][idx2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n= len(text1); m = len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                take = dp[i+1][j+1]+1 if text1[i]==text2[j] else 0
                not_take = max(dp[i][j+1], dp[i+1][j])

                dp[i][j]= max(take, not_take)

        return dp[0][0]