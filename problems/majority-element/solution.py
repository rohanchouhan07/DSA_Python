from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # cnt = Counter(nums)
        # n = len(nums)
        # for num, freq in cnt.items():
        #     if freq > n // 2:
        #         return num
        # n=len(nums)
        ele=0
        cnt=0
        for num in nums:
            if cnt==0:
                ele=num
                cnt+=1
            elif num == ele:
                cnt+=1
            else:
                cnt-=1
        return ele