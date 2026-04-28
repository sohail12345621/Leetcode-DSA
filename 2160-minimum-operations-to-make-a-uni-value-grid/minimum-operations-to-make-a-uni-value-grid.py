class Solution:
    def minOperations(self, grid, x):
        # Step 1: Flatten the grid
        arr = [num for row in grid for num in row]
        
        # Step 2: Check feasibility
        remainder = arr[0] % x
        for num in arr:
            if num % x != remainder:
                return -1
        
        # Step 3: Sort and find median
        arr.sort()
        median = arr[len(arr) // 2]
        
        # Step 4: Calculate operations
        operations = 0
        for num in arr:
            operations += abs(num - median) // x
        
        return operations