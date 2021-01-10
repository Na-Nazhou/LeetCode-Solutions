class Solution {
    private boolean reachable(String s1, String s2) {
        if (s1.length() != s2.length()) {
            return false;
        }
        boolean hasDiff = false;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (hasDiff) {
                    return false;
                } else {
                    hasDiff = true;
                }
            }
        }
        return true;
    }
    
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        List<List<Integer>> adjList = new ArrayList<>();
        int beginIndex = wordList.indexOf(beginWord);
        int endIndex = -1;
        
        if (beginIndex == -1) {
            beginIndex = wordList.size();
            wordList.add(beginWord);
        }
        
        for (int i = 0; i < wordList.size(); i++) {
            String word = wordList.get(i);
            if (word.equals(endWord)) {
                endIndex = i;
            }
            List<Integer> neighbours = new ArrayList<>();
            for (int j = 0; j < wordList.size(); j++) {
                if (reachable(word, wordList.get(j))) {
                    neighbours.add(j);
                }
            }
            adjList.add(neighbours);
        }
        
        if (endIndex == -1) {
            return 0;
        }
        
        Queue<Integer> queue = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();
        queue.offer(beginIndex);
        visited.add(beginIndex);
        
        int count = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            count++;
            for (int i = 0; i < size; i++) {
                int curr = queue.poll();
                for (int neighborIndex : adjList.get(curr)) {
                    if (neighborIndex == endIndex) {
                        return count;
                    }
                    if (visited.contains(neighborIndex)) {
                        continue;
                    }
                    queue.offer(neighborIndex);
                    visited.add(neighborIndex);
                }
            }
        }
        return 0;
    }
}
