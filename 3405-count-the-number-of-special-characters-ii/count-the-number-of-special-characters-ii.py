class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        lower_last = {}
        upper_first = {}
        
        # Store positions
        for i, ch in enumerate(word):
            
            if ch.islower():
                lower_last[ch] = i
            
            else:
                small = ch.lower()
                
                # store first uppercase occurrence only
                if small not in upper_first:
                    upper_first[small] = i
        
        count = 0
        
        # Check condition
        for ch in lower_last:
            
            if ch in upper_first:
                
                if lower_last[ch] < upper_first[ch]:
                    count += 1
        
        return count