from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)
        min_dist = float('inf')
        for pos in positions.values():
            if len(pos) >= 3:
                for i in range(len(pos) - 2):
                    dist = 2 * (pos[i + 2] - pos[i])
                    min_dist = min(min_dist, dist)
        return min_dist if min_dist != float('inf') else -1