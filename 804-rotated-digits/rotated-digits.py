class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0', '1', '2', '5', '6', '8', '9'}
        change = {'2', '5', '6', '9'}
        
        count = 0
        
        for num in range(1, n + 1):
            s = str(num)
            is_valid = True
            is_good = False
            
            for ch in s:
                if ch not in valid:
                    is_valid = False
                    break
                if ch in change:
                    is_good = True
            
            if is_valid and is_good:
                count += 1
        
        return count