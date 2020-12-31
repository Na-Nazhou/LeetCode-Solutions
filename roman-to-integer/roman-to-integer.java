class Solution {
    
    private static final Map<Character, Integer> map = Map.of('I', 1, 
                                                              'V', 5, 
                                                              'X', 10, 
                                                              'L', 50, 
                                                              'C', 100,  
                                                              'D', 500,
                                                              'M', 1000
                                                            );
    
    public int romanToInt(String s) {
        int sum = 0;
        int i = 0;
        while (i < s.length()) {
            int curr = map.get(s.charAt(i));
            if (i == s.length() - 1) {
                sum += curr;
                break;
            }
            
            int next = map.get(s.charAt(i + 1));
            if (curr < next) {
                sum += (next - curr);
                i += 2;
            } else {
                sum += curr;
                i++;
            }
        }
        
        return sum;
    }
}
