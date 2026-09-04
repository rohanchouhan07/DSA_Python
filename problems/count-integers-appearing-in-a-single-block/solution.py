class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        """
        [3,3,3,1,2,2,1] --> [1,2,3]
        3 --> 0,2, 3
        1 --> 3,6, 2
        2 --> 4,5, 2
        3,2 -- special
        1 -- Not special
        """
        arr = set(nums)
        N = len(nums)
        ans = 0
        def calc(val):
            first, last = -1, -1
            count = 0
            for i in range(0, N):
                if(nums[i] == val):
                    last = i
                    count += 1
                    if first == -1:
                        first = i
                    
            return [first, last, count]
        for v in arr:
            x = calc(v)
            #print(x)
            l = x[1] - x[0] + 1
            if l == x[2]:
                ans += 1
        return ans