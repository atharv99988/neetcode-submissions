class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # function that will give all lengths of matching words from i to end
        def lengthOfMatchingWords(i) : 
            ans = []
            for word in wordDict : 
                want = True
                pos = i
                for j in range(len(word)) : 
                    if pos >= len(s) or word[j] != s[pos] : 
                        want = False
                        break
                    pos += 1
                if want : 
                    ans.append(len(word))
            return ans 
        # do dry run

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s)-1,-1,-1) : 
            lengths = lengthOfMatchingWords(i)
            for length in lengths: 
                if i + length <= len(s) and dp[i + length] : 
                    dp[i] = True
                    break
        
        return dp[0]
            
                

