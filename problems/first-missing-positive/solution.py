class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums=set(nums)
        # if 1 not in nums:
        #     return 1

        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         return i
        # return max(nums)+1
        nums.sort()
        