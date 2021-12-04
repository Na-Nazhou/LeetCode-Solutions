class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self.insert_word(word)
        self.data = []
    
    def insert_word(self, word):
        curr = self.root
        for i in range(len(word) - 1, -1, -1):
            idx = ord(word[i]) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.endOfWord = True

    def query(self, letter: str) -> bool:
        self.data.append(letter)
        curr = self.root
        for i in range(len(self.data) - 1, -1, -1):
            idx = ord(self.data[i]) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
            if curr.endOfWord:
                return True
        
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)