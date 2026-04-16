class Solution:
    def twoSum(self, nums: List[int], tgt: int) -> List[int]:
        hs = {}
        for idx in range(len(nums)):
            q = tgt - nums[idx]
            if q in hs:
                return ([hs[q], idx])

            hs[nums[idx]]=idx
        
