from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if s == "" and t == "" : 
            return True

        length = len(s)
        if length != len(t) : 
            return False

        s_hashmap = Counter(s) 
        t_hashmap = Counter(t)

        for key in s_hashmap.keys() : 
            if key not in t_hashmap or t_hashmap.get(key) != s_hashmap.get(key) : 
                return False
            
        return True

        