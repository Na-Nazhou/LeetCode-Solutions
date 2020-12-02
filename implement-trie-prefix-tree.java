class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean endOfWord = false;
}
​
class Trie {
    TrieNode root;
​
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
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
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode curr = root;
        for (char ch : word.toCharArray()) {
            int child = ch - 'a';
            if (curr.children[child] == null) {
                return false;
            }
            curr = curr.children[child];
        }
        return curr.endOfWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for (char ch : prefix.toCharArray()) {
            int child = ch - 'a';
            if (curr.children[child] == null) {
                return false;
            }
            curr = curr.children[child];
        }
        return true;
    }
}
​
/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
