class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean endOfWord = false;
}
​
class WordDictionary {
     TrieNode root;
​
    /** Initialize your data structure here. */
    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode curr = root;
        for (char ch : word.toCharArray()) {
            int child = ch - 'a';
            if (curr.children[child] == null) {
                curr.children[child] = new TrieNode();
            }
            curr = curr.children[child];
        }
        curr.endOfWord = true;
    }
    
    public boolean search(String word) {
        return search(word.toCharArray(), 0, root);
    }
    
    private boolean search(char[] word, int start, TrieNode node) {
        TrieNode curr = node;
        for (int i = start; i < word.length; i++) {
            int ch = word[i];
            if (ch == '.') {
                boolean found = false;
                for (TrieNode child : curr.children) {
                    if (child != null && search(word, i + 1, child)) {
                        found = true;
                        break;
                    }
                }
                return found;
            } 
            
            int child = ch - 'a';
            if (curr.children[child] == null) {
                return false;
            }
            curr = curr.children[child];
        }
        return curr.endOfWord;
    }
}
​
/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
