class Solution:
    def check(self, a: List[int]) -> bool:
        count = 0
        # for i in range(0, len(nums)-1):
        #     if nums[i] > nums[i + 1] % len(nums):
        #         cnt += 1
        # if cnt <= 1:
        #     return True
        # return False

        for i in range(0,len(a)):
            if a[i]>a[(i+1)%len(a)]:
                count+=1
        if(count<=1):
            return True
        return False