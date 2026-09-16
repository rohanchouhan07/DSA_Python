import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Its easy but cannt do because que says without Sorting
        # nums.sort(reverse=True)
        # return nums[k-1]

        # Use Heap becaues it Quikly get the smallest or largest element
        
        min_heap=[]
        for i in nums:
            heapq.heappush(min_heap,i)
            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return min_heap[0]