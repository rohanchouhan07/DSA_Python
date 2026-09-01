class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cntz=0
        cnt=nums.count(0)
        while 0 in nums:
            nums.remove(0)
            cntz+=1

        nums.extend([0]*cntz)
    