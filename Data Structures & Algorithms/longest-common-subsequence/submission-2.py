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
        dp = [[-1]*(m) for _ in range(n)]

        for idx1 in range(n):
            dp[idx1][0] =1 if text1[idx1]==text2[0] else 0
        
        for idx2 in range(m):
            dp[0][idx2] =1 if text1[0]==text2[idx2] else 0
        
        txt1 = text1; txt2 = text2
        for idx1 in range(n):
            for idx2 in range(m):
                take = self.rec(txt1, txt2, idx1-1, idx2-1, dp)+1 if txt1[idx1]==txt2[idx2] else 0
                not_take = max(self.rec(txt1, txt2, idx1-1, idx2, dp), self.rec(txt1, txt2, idx1, idx2-1, dp))

                dp[idx1][idx2]= max(take, not_take)

        return dp[-1][-1]