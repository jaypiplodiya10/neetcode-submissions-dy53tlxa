class Solution:
    def rec(self, nums, idx, dp):
        if idx < 0: return 0

        if dp[idx] != -1: return dp[idx]

        take = self.rec(nums, idx-2, dp) + nums[idx]
        not_take = self.rec(nums, idx-1, dp) + 0

        dp[idx]= max(take, not_take)
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)-1; dp=[-1]*(n+1)

        return self.rec(nums,n, dp)