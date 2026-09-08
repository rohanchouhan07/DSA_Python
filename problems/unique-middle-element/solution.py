class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        N = len(nums)
        mid = nums[N//2]
        return nums.count(mid) == 1