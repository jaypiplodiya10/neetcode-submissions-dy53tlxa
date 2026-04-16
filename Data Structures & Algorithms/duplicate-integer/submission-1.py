class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = {}
        for ele in nums:
            if ele in hs:
                return True
            else:
                hs[ele] =1
        
        return False
            