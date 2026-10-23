class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cs=mx=nums[0]
        n=len(nums)
        for i in range(1,n):
            cs=max(cs+nums[i],nums[i])
            mx=max(mx,cs)
        
        return mx
