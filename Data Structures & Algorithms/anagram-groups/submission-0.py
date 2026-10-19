class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for word in strs :
            key = tuple(sorted(word))
            if key not in hash : 
                hash[key] = [word]
            else  :
                hash[key].append(word)

        ans = []
        for values in hash.values() : 
            ans.append(values)
        
        return ans           

        