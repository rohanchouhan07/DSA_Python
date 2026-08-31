class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        m=max(nums)
        i=nums.index(m)
        return i