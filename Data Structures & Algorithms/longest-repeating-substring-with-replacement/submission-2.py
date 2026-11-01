class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cha = {}

        l = 0
        res = 0

        for r in range(len(s)) : 
            cha[s[r]] = cha.get(s[r],0) + 1
            
            while (r-l+1) - max(cha.values()) > k :
                cha[s[l]] -= 1
                l += 1
            
            res = max(res, (r-l+1))

        return res


        