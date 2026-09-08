class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        return sum(nums[N-k:N]) - sum(nums[0:k])