class Solution:
    def rec(self, nums, idx, dp):
        if idx < 0: return 0

        if dp[idx] != -1: return dp[idx]

        take = self.rec(nums, idx-2, dp) + nums[idx]
        not_take = self.rec(nums, idx-1, dp) + 0

        dp[idx]= max(take, not_take)
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        n = len(nums); dp=[-1]*(n+1)

        if n==1: return nums[0]
        if n==2: return max(nums[0], nums[1])

        prev1=nums[0]; prev2=max(nums[0], nums[1])

        curr = -1
        for idx in range(2, n):
            take = nums[idx]+prev1
            not_take = prev2

            curr = max(take, not_take)
            prev1, prev2= prev2, curr

        return prev2