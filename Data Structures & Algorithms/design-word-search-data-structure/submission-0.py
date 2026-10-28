class TreeNode : 
    def __init__(self) : 
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word : 
            if i not in curr.children : 
                curr.children[i] = TreeNode()
            curr =  curr.children[i]
        curr.word = True   

    def search(self, word: str) -> bool:

        def dfs(j, root) :
            curr = root
            for i in range(j, len(word)) : 
                #  if we have a .
                if word[i] == '.' : 
                    for node in curr.children.values() : 
                        if dfs(i+1, node) : 
                            return True
                    return False
                else : 
                    if word[i] not in curr.children :
                        return False
                    else :
                        curr = curr.children[word[i]]

            return curr.word
        
        return dfs(0, self.root)
