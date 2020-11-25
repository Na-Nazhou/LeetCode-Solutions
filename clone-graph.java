/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/
​
class Solution {
    public Node cloneGraph(Node node) {
        return cloneGraph(node, new HashMap<>());
    }
    
    public Node cloneGraph(Node node, Map<Integer, Node> map) {
        if (node == null) {
            return null;
        }
        
        if (map.containsKey(node.val)) {
            return map.get(node.val); 
        }
        
        Node clone = new Node(node.val);
        map.put(node.val, clone);
        
        for (Node neighbor : node.neighbors) {
            clone.neighbors.add(cloneGraph(neighbor, map));
        }
        
        return clone;
    }
}
