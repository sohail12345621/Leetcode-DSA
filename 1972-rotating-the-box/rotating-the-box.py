from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        # Step 1: Simulate gravity (stones fall to the right)
        for i in range(m):
            empty = n - 1  # position where next stone should go

            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    empty = j - 1  # reset position after obstacle
                elif box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][empty] = '#'
                    empty -= 1

        # Step 2: Rotate 90 degrees clockwise
        rotated = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = box[i][j]

        return rotated