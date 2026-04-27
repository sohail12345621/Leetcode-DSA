from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Direction mapping
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        visited = [[False]*n for _ in range(m)]
        q = deque([(0, 0)])
        visited[0][0] = True
        
        while q:
            x, y = q.popleft()
            
            if x == m - 1 and y == n - 1:
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    
                    # Check reverse connection
                    for rdx, rdy in dirs[grid[nx][ny]]:
                        if nx + rdx == x and ny + rdy == y:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            break
        
        return False