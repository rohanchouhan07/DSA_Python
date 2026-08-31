class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i=max(arr)
        return arr.index(i)