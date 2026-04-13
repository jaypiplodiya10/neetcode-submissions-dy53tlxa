class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums); res=nums[0]
        pref = suf =0

        for idx in range(n):
            pref = nums[idx]*(pref or 1)
            suf = nums[n-1-idx]*(suf or 1)

            res = max(res, pref, suf)
        
        return res