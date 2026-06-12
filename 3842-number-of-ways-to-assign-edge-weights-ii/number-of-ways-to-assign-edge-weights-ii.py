from typing import List
import sys

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        n = len(edges) + 1
        
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        LOG = (n + 1).bit_length()
        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        
        # DFS/BFS to build depth and immediate parent
        stack = [1]
        visited = [False] * (n + 1)
        visited[1] = True
        
        while stack:
            u = stack.pop()
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[0][v] = u
                    stack.append(v)
        
        # Binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                parent[j][i] = parent[j - 1][parent[j - 1][i]]
        
        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]
            
            if u == v:
                return u
            
            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]
            
            return parent[0][u]
        
        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        
        ans = []
        
        for u, v in queries:
            w = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[w]  # number of edges
            
            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow2[dist - 1])
        
        return ans