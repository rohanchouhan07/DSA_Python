class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        # 5//2 --> 2, 5/2 = 2.5
        for i in range(0, N-1):
            sum,count = 0,0
            for j in range(i+1, N):
                sum += nums[j]
                count += 1
            avg = sum / count
            if avg < nums[i]:
                ans += 1
        return ans