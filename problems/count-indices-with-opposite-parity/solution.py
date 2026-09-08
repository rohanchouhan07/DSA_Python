class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        """
        [1,2,3,4]
        [1,0,1,0]
        [2,1,1,0]

        
        for i in range(0, N):

        [1,3,2,4,5,6,8,10]
        """
#         ans = []
#         N = len(nums)
#         for i in range(0,N):
#             count = 0
#             for j in range(i+1, N):
#                 if nums[i]%2 != nums[j]%2:
#                     count += 1
#             ans.append(count)
#         return ans
    
        odd, even = 0, 0
        for v in nums:
            if v%2 == 0:
                even += 1
            else:
                odd += 1
        ans = []
        for v in nums:
            if v%2 != 0:
                ans.append(even)
                odd -= 1
            else:
                ans.append(odd)
                even -= 1
        return ans