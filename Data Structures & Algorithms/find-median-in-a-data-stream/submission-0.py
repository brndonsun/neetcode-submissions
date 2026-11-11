import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = [] #right side
        self.max_heap = [] #left side negative version of the value
        

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
           heapq.heappush(self.min_heap, num)
        else:
           heapq.heappush(self.max_heap, -1 * num)

        #rebalance
        if len(self.min_heap) > len(self.max_heap) + 1:
            switch = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * switch)
        if len(self.max_heap) > len(self.min_heap) + 1:
            switch = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -1 * switch)


    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + (-1 * self.max_heap[0])) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -1 * self.max_heap[0]

        
        