class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            switch (ch) {
                case '(':
                    stack.push(')');
                    break;
                case '{':
                    stack.push('}');
                    break;
                case '[':
                    stack.push(']');
                    break;
                case ')': case '}': case ']':
                    if (stack.isEmpty() || stack.pop() != ch) {
                        return false;
                    }
                    break;
                default:
                    throw new IllegalArgumentException("Unexpected character!");
            }
        }
        
        return stack.isEmpty();
    }
}
