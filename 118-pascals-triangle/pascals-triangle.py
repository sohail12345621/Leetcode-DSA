class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for i in range(numRows):

            # Every row starts with 1
            row = [1] * (i + 1)

            # Fill middle values
            for j in range(1, i):

                row[j] = (
                    triangle[i - 1][j - 1] +
                    triangle[i - 1][j]
                )

            triangle.append(row)

        return triangle