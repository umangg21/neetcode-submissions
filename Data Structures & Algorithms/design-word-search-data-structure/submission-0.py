class TrieNode: 
    def __init__(self):
        self.children = {}
        self.eow = False 


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.eow = True

        return None
                
    def search(self, word: str) -> bool:
        curr = self.root
        l = len(word)

        def backTrack(i, curr):
            if i == l: return curr.eow

            if word[i] == ".":
                for child in curr.children.values():
                    if backTrack(i+1, child):
                        return True
                return False
            
            else:
                if word[i] not in curr.children:
                    return False
                
                return backTrack(i+1, curr.children[word[i]])


        
        res = backTrack(0, curr)
        return res
