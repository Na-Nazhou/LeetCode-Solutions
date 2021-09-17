class TrieNode:
    
    def __init__(self):
        self.children = [None]* 26
        self.eow = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.eow = True

    def search(self, word: str) -> bool:
        def helper(node, i) -> bool:
            if node is None:
                return False

            if i == len(word):
                return node.eow

            if word[i] == ".":
                for child in node.children:
                    if helper(child, i+1):
                        return True
                return False
            else:
                idx = ord(word[i]) - ord('a')
                return helper(node.children[idx], i+1)
            
        return helper(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)