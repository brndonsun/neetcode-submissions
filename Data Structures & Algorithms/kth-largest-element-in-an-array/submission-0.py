import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minheap = []
        for number in nums:
            heapq.heappush(minheap, number)

        for i in range(len(nums) - k):
            heapq.heappop(minheap)

        return heapq.heappop(minheap)