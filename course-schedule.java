class Solution {
    public ArrayList<ArrayList<Integer>> adjList;
    public Set<Integer> preVisited = new HashSet<>();
    public Set<Integer> postVisited = new HashSet<>();
    public boolean foundCycle = false;
        
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        adjList = new ArrayList<>();
        preVisited = new HashSet<>();
        postVisited = new HashSet<>();
        foundCycle = false;
        
        for (int i = 0; i < numCourses; i++) {
            adjList.add(new ArrayList<>());
        }
        
        for (int[] prerequisite : prerequisites) {
            adjList.get(prerequisite[0]).add(prerequisite[1]);
        }
        
       for (int i = 0; i < numCourses; i++) {
            dfs(i);
        }
        
        return !foundCycle;    
    }
    
    public void dfs(int root) {
        if (postVisited.contains(root)) {
            return;
        }
        
        if (preVisited.contains(root)) {
            foundCycle = true;
            return;
        }
        
        preVisited.add(root);
        
        for (int neighbor : adjList.get(root)) {
            dfs(neighbor);
        }
        
        preVisited.remove(root);
        postVisited.add(root);
    }
}
