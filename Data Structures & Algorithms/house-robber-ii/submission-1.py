class Solution:
    def helper(self, nums):
        n = len(nums)
        prev1=nums[0]; prev2=max(nums[0], nums[1])
        for idx in range(2, n):
            take = nums[idx]+prev1
            not_take = prev2

            curr = max(take, not_take)
            prev1, prev2= prev2, curr
        
        return prev2

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums[0], nums[1])
        
        first = self.helper(nums[1:])
        last = self.helper(nums[:-1])

        return max(first, last)