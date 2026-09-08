class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        N = len(nums)
        MAX = N*5
        ans = MAX
        for i in range(0, N):
            for j in range(i+1, N):
                if nums[i] == nums[j]:
                    for k in range(j+1, N):
                        if nums[j] == nums[k]:
                            x = abs(i-j) + abs(j-k) + abs(k-i)
                            ans = min(ans, x)
        if ans == MAX:
            ans = -1
        return ans