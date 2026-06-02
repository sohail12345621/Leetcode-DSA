import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        
        # Count frequency
        freq = Counter(nums)

        heap = []

        # Push frequency and number into heap
        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))

        ans = []

        # Take top k frequent elements
        for _ in range(k):
            count, num = heapq.heappop(heap)
            ans.append(num)

        return ans