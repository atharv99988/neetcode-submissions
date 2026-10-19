from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs : 
            hash_word = Counter(word)
            key = tuple(sorted(hash_word.items()))
            hashmap[key].append(word)
        return list(hashmap.values())
        