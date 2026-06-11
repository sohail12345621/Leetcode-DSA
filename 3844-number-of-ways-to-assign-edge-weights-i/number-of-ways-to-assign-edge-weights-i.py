class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7

        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        max_depth = 0

        stack = [(1, 0, -1)]  # node, depth, parent

        while stack:
            node, depth, parent = stack.pop()

            max_depth = max(max_depth, depth)

            for nei in graph[node]:
                if nei != parent:
                    stack.append((nei, depth + 1, node))

        return pow(2, max_depth - 1, MOD)