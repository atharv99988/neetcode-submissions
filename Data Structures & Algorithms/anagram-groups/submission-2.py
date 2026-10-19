from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs : 
            key = str(sorted(word))
            hashmap[key].append(word)
        return list(hashmap.values())
        