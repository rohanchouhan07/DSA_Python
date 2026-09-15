class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # nums[:]=set(nums)
        # return len(nums)
        pos=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[pos]=nums[i]
                pos+=1
        return pos

        # if(len(a)==0):
        #   return 0
        # pos=1
        # for i in range(1,len(a)):
        #   if(a[i]!=a[i-1]):
        #     a[pos]=a[i]
        #     pos+=1
        # return pos