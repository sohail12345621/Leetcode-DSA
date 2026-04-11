class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # will store indices
        max_area = 0
        
        # Add a dummy 0 height to flush stack at end
        heights.append(0)
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                
                # width calculation
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                
                max_area = max(max_area, h * width)
            
            stack.append(i)
        
        return max_area