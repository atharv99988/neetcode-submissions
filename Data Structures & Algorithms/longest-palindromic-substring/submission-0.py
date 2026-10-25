class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        ans = ""
        length = len(s)
        for i in range(length) : 
            l,r = i,i
            # finding odd length palindromes 
            while l >= 0 and r < length and s[l] == s[r] :
                if max_length <= r-l+1 : 
                    ans = s[l:r+1]
                    max_length = max(max_length, r-l+1)
                l -= 1
                r += 1

            l,r = i, i+1

            # finding for even lengths
            while l >= 0 and r < length and s[l] == s[r] :
                if max_length <= r-l+1 : 
                    ans = s[l:r+1]
                    max_length = max(max_length, r-l+1)
                l -= 1
                r += 1

        return ans


                
        