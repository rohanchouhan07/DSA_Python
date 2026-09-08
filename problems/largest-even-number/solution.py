class Solution:
    def largestEven(self, s: str) -> str:
        """
        check the last digit is even or not

        1121 --> 112

        1212

        1211 --> 121 -->12
        """
        index = -1
        N = len(s)
        for i in range(N-1, -1, -1):
            val = int (s[i])
            if val%2 == 0:
                index = i
                break
        return s[0:index+1]