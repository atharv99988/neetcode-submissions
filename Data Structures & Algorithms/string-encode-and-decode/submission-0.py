class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ''
        for i in strs : 
            encode_string += str(len(i)) + '#' + i
        return encode_string

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s) : 
            j = i
            while s[j] != '#' : 
                j += 1
            
            length = int(s[i:j])
            i = j + 1 # skip the #
            j = i + length
            ans.append(s[i:j])
            i = j

        return ans  
