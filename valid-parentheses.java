class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                
                char match = stack.pop();
                if (ch == ')' && match != '(') {
                    return false;
                }
                
                if (ch == '}' && match != '{') {
                    return false;
                }
                
                if (ch == ']' && match != '[') {
                    return false;
                }
                
            }
        }
        
        return stack.isEmpty();
    }
}
