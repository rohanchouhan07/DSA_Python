class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        # ----------------------soln------------------------
        # for i in nums:
        #     if len(str(i))%2==0:
        #         cnt+=1
        # return cnt
        

        # ------------------optimal soln -------------------
        for i in nums:
            if (10 <= i <= 99) or (1000 <= i <= 9999) or (i == 100000):
                cnt+=1
        return cnt 