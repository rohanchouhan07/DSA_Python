class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # min of k is such that banana pile will finish in h hr
        c=1
        ans=0
        def maxx(piles):
            max=piles[0]
            for i in piles:
                if max<i:
                    max=i
            return max

        def cal(k,piles):
            s=0
            for i in piles:
                s+=(i+k-1)//k
            return s


        # for k in range(1,maxx(piles)+1):
        #     if cal(k,piles)==h:
        #         return k
        l=1
        r=maxx(piles)
        ans=0
        while (l<=r):
            mid=(l+r)//2
            # if cal(mid,piles)==h:
                # return mid
                # break
            if(cal(mid,piles) <= h):
                r=mid-1
                ans=mid
            else:
                l=mid+1
        return ans
