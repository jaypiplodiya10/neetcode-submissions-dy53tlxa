class Solution:
    def rec(self, coins, tgt, idx, dp):
        if idx < 0: return float('inf')
        if tgt==0: return 0

        if dp[tgt][idx] != -1: return dp[tgt][idx]

        take = self.rec(coins, tgt-coins[idx], idx, dp) +1 if coins[idx] <= tgt else float('inf')
        not_take = self.rec(coins, tgt,idx-1, dp)

        dp[tgt][idx] = min(take, not_take)
        return  dp[tgt][idx]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * n for _ in range(amount + 1)]
        
        for idx in range(n):
            dp[0][idx]=0
        
        for idx in range(amount+1):
            if idx % coins[0]==0:
                dp[idx][0]= idx//coins[0]
        
        for i in range(n):
            for j in range(amount+1):
                not_take = dp[j][i-1]
                take = dp[j-coins[i]][i]+1 if coins[i] <= j else float('inf')

                dp[j][i] = min(take, not_take)

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
        # ans = self.rec(coins, amount, len(coins)-1, dp)
        # return -1 if ans==float('inf') else ans