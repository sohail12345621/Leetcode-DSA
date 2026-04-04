class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        # Step 1: Build the matrix
        matrix = []
        index = 0
        
        for i in range(rows):
            matrix.append(encodedText[index:index + cols])
            index += cols
        
        # Step 2: Traverse diagonally
        result = []
        
        for col in range(cols):
            i, j = 0, col
            while i < rows and j < cols:
                result.append(matrix[i][j])
                i += 1
                j += 1
        
        # Step 3: Remove trailing spaces
        return ''.join(result).rstrip()