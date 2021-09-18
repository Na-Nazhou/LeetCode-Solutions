class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        result = []
        billion = num // 10 ** 9
        num = num % 10 ** 9
        
        if billion > 0:
            result += self.numberToWordsWithinTen(billion)
            result.append("Billion")
        
        million = num // 10 ** 6
        num = num % 10 ** 6
        if million > 0:
            result += self.numberToWordsWithinThousand(million)
            result.append("Million")
        
        thousand = num // 10 ** 3
        num = num % 10 ** 3
        if thousand > 0:
            result += self.numberToWordsWithinThousand(thousand)
            result.append("Thousand")
        
        result += self.numberToWordsWithinThousand(num)
        
        return " ".join(result)
            
    
    def numberToWordsWithinThousand(self, num):
        hundred = num // 100
        result = []
        if hundred > 0:
            result += self.numberToWordsWithinTen(hundred)
            result.append("Hundred")
        result += self.numberToWordsWithinHundred(num % 100)
        return result
    
    def numberToWordsWithinHundred(self, num):
        result = []
        if num > 10 and num < 20:
            result += self.numberToWordsFromTenToTwenty(num)
            return result
        
        ten = num // 10
        m = {
            1: "Ten",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
       
        if ten > 0:
            result.append(m[ten])
        
        result += self.numberToWordsWithinTen(num % 10)
        return result
    
    def numberToWordsFromTenToTwenty(self, num):
        m = {
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        
        result = [m[num]]
        return result
    
    def numberToWordsWithinTen(self, num):
        m = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"            
        }
        
        result = []
        if num > 0:
            result.append(m[num])
        
        return result