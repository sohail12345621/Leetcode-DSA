class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1]
        max_len = 0

        for i in range(len(s)):

            # If opening bracket
            if s[i] == '(':
                stack.append(i)

            else:
                # Pop previous bracket
                stack.pop()

                # If stack becomes empty
                if not stack:
                    stack.append(i)

                else:
                    # Calculate valid length
                    length = i - stack[-1]
                    max_len = max(max_len, length)

        return max_len