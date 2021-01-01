class Solution {
    private List<String> answer = new ArrayList<>();
    
    public List<String> generateParenthesis(int n) {
        generateParenthesis(n, n, 0, new StringBuilder());
        return answer;
    }
    
    private void generateParenthesis(int opening, int closing, int balance, StringBuilder curr) {
        if (opening == 0 && closing == 0 && balance == 0) {
            answer.add(curr.toString());
            return;
        }
        
        if (opening > 0) {
            curr.append('(');
            generateParenthesis(opening - 1, closing, balance + 1, curr);
            curr.deleteCharAt(curr.length() - 1);
        }
        
        if (balance > 0) {
            curr.append(')');
            generateParenthesis(opening, closing - 1, balance - 1, curr);
            curr.deleteCharAt(curr.length() - 1);
        }
    }
}
