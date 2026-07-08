class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = {}
        
        # 1. ADDING TALLIES
        for x in s:
            if x in count:   # <--- CHECK THE DICTIONARY, NOT 's'
                count[x] += 1
            else:
                count[x] = 1
        
        # 2. SUBTRACTING TALLIES
        for x in t:
            if x in count:   # <--- CHECK THE DICTIONARY, NOT 't'
                count[x] -= 1
            else:
                return False
        
        # 3. THE AUDIT
        for val in count.values():
            if val != 0:
                return False 
                
        return True