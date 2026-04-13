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
        dp = [float('inf')]*(amount+1)

        dp[0]=0
        for idx in range(amount+1):
            for coin in coins:
                if coin <= idx:
                    dp[idx] = min(dp[idx],1+ dp[idx-coin])
        
        return dp[-1] if dp[-1] != float('inf') else -1
        # ans = self.rec(coins, amount, len(coins)-1, dp)
        # return -1 if ans==float('inf') else ans