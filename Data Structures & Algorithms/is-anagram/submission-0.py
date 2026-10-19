class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False 

        hash1 = {}
        hash2 = {}

        for c in s : 
            if c not in hash1 : 
                hash1[c] = 1
            else : 
                hash1[c] += 1

        for c in t : 
            if c not in hash2 : 
                hash2[c] = 1
            else : 
                hash2[c] += 1

        for c,count in hash1.items()  :
            if not (c in hash2 and hash2[c] == count) :
                return False
        
        return True

        