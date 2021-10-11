class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.is_word = True

    def search(self, word: str) -> bool:
        
        def helper(curr, i):
            if curr is None:
                return False
            
            if i == len(word):
                return curr.is_word
            
            c = word[i]
            if c == '.':
                for child in curr.children:
                    if helper(child, i + 1):
                        return True
                return False
            else:
                idx = ord(c) - ord('a')
                return helper(curr.children[idx], i + 1)
        
        return helper(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)