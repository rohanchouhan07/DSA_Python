class Solution:
    def maxArea(self, height: List[int]) -> int:
        mw=0
        l=0
        r=len(height)-1
        while(l<r):
            w=r-l
            h=min(height[l],height[r])

            area=w*h
            mw=max(mw,area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return mw