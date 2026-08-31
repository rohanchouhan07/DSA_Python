class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        f=0
        l=n-1
        while(f<l):
            s[f],s[l]=s[l],s[f]
            f+=1
            l-=1
        