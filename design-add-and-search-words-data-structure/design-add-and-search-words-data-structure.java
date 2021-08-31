class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean eow = false;
}

class WordDictionary {
    TrieNode root;

    /** Initialize your data structure here. */
    public WordDictionary() {
        this.root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode curr = this.root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int idx = ch - 'a';
            
            if (curr.children[idx] == null) {
                curr.children[idx] = new TrieNode();
            }
            
            curr = curr.children[idx];
        }
        
        curr.eow = true;
    }
    
    public boolean search(String word) {        
        return search(word, 0, root);
    }
    
    private boolean search(String word, int i, TrieNode curr) {
        if (curr == null) {
            return false;
        }
        
        if (i == word.length()) {
            return curr.eow;
        }
        
        char ch = word.charAt(i);
        if (ch == '.') {
            for (TrieNode node : curr.children) {
                if (search(word, i + 1, node)) {
                    return true;
                }
            }
                    
            return false;
        } else {
            int idx = ch - 'a';
            curr = curr.children[idx];
            return search(word, i + 1, curr);
        }
            
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */