class Solution:
    def rec(self, nums, idx, prev, dp):
        if idx == len(nums): return 0

        if dp[idx][prev+1] != -1: return dp[idx][prev+1]
        take = self.rec(nums, idx+1, idx, dp)+1 if (nums[idx] > nums[prev] or prev ==-1) else 0
        not_take = self.rec(nums, idx+1, prev, dp)

        dp[idx][prev+1] = max(take, not_take)
        return dp[idx][prev+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(n+1)]

        # return self.rec(nums, 0, -1, dp)

        for i in range(n-1, -1, -1):
            for j in range(i-1, -2, -1):
                not_take = dp[i+1][j+1]
                take = dp[i+1][i+1] +1 if (nums[i]>nums[j] or j ==-1) else 0

                dp[i][j+1] = max(take, not_take)
        
        return dp[0][0]
