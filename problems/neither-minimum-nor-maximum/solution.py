class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minV , maxV = nums[0], nums[0]
        minV=min(nums)
        maxV=max(nums)
        for v in nums:
            if v != minV and v != maxV:
                return v
        return -1