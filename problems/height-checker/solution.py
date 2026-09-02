class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n=len(heights)
        ex=heights[0:n]
        ex.sort()
        cnt=0
        for i in range(n):
            if ex[i] != heights[i]:
                cnt+=1

        return cnt