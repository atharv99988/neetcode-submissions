class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t :
            return ""
        hash_s, hash_t = {}, Counter(t)

        l = 0
        have, need = 0, len(hash_t.items())
        comp = [[0,0], float("inf")]

        for r in range(len(s)):
            if s[r] in hash_t:
                hash_s[s[r]] = hash_s.get(s[r],0) + 1
                if hash_s.get(s[r],0) == hash_t[s[r]] : 
                    have += 1 
        
            # removing characters till the output is valid
            while have == need:
                if (r - l + 1) < comp[1]:
                    comp = [[l, r], r - l + 1]

                if s[l] in hash_t:
                    hash_s[s[l]] -= 1
                    if hash_s[s[l]] < hash_t[s[l]]:
                        have -= 1

                l += 1

        return s[comp[0][0] : comp[0][1] + 1]  if comp[1] != float("inf") else ""
                    


        
        