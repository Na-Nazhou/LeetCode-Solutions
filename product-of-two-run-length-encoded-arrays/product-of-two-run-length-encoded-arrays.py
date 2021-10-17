class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i_1 = 0 # which pair
        j_1 = 0 # which instance
        i_2 = 0
        j_2 = 0
        
        ans = []
        while i_1 < len(encoded1) and i_2 < len(encoded2):
            val_1, freq_1 = encoded1[i_1]
            val_2, freq_2 = encoded2[i_2]
            
            product = val_1 * val_2
            freq = min(freq_1 - j_1, freq_2 - j_2)
            
            if freq_1 - j_1 > freq_2 - j_2:
                j_1 += freq
                
                i_2 += 1
                j_2 = 0
            elif freq_1 - j_1 < freq_2 - j_2:
                i_1 += 1
                j_1 = 0
                
                j_2 += freq
            else:
                i_1 += 1
                i_2 += 1
                j_1 = 0
                j_2 = 0
            
            if ans and ans[-1][0] == product:
                ans[-1][1] += freq
            else:
                ans.append([product, freq])
        
        return ans