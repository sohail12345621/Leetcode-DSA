class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        v = 0

        for ch in s:
            if ch=="(":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    v += 1

        return len(stack) + v