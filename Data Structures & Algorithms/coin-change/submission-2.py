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
        dp = [[-1]*n for _ in range(amount+1)]

        ans = self.rec(coins, amount, len(coins)-1, dp)
        return -1 if ans==float('inf') else ans