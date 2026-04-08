class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        for num in nums:
            if mini > num:
                mini = num
        return mini
        