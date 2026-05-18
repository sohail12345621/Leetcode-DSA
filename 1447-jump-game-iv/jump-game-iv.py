from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n == 1:
            return 0
        
        # Store indices for each value
        graph = defaultdict(list)
        
        for i, val in enumerate(arr):
            graph[val].append(i)
        
        # BFS
        q = deque([(0, 0)])  # (index, steps)
        visited = set([0])
        
        while q:
            idx, steps = q.popleft()
            
            # Reached last index
            if idx == n - 1:
                return steps
            
            neighbors = []
            
            # Same value jumps
            neighbors.extend(graph[arr[idx]])
            
            # Adjacent jumps
            if idx + 1 < n:
                neighbors.append(idx + 1)
            
            if idx - 1 >= 0:
                neighbors.append(idx - 1)
            
            for nei in neighbors:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, steps + 1))
            
            # Important optimization:
            # Clear list so we don't process same-value indices again
            graph[arr[idx]].clear()
        
        return -1