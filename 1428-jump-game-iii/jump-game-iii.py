from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        queue = deque([start])

        while queue:
            i = queue.popleft()

            if arr[i] == 0:
                return True

            if i in visited:
                continue

            visited.add(i)

            forward = i + arr[i]
            backward = i - arr[i]

            if 0 <= forward < n:
                queue.append(forward)

            if 0 <= backward < n:
                queue.append(backward)

        return False