from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        n=len(nums)
        for num, freq in cnt.items():
            if freq > n // 2:
                return num