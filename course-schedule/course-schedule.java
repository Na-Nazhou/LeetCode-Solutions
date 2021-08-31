class Solution {
    List<List<Integer>> g = new ArrayList<>();
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        g = new ArrayList<>();
        
        for (int i = 0; i < numCourses; i++) {
            g.add(new ArrayList<>());
        }
        
        for (int[] courses : prerequisites) {
            g.get(courses[0]).add(courses[1]);
        }
        
        int[] visited = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (visited[i] == 0) {
                if (containsCycle(i, visited)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean containsCycle(int course, int[] visited) {
        if (visited[course] == 2) {
            return false;
        } 
        
        if (visited[course] == 1) {
            return true;
        }
        
        visited[course] = 1;
        
        for (int neighbor : g.get(course)) {
            if (containsCycle(neighbor, visited)) {
                return true;
            }
        }
        
        visited[course] = 2;
        
        return false;
    }
}