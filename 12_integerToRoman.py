class Solution:
    def intToRoman(self, num: int) -> str:
        decimal = [1000, 500, 100, 50, 10, 5, 1]
        roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        output = ''
        
        for idx, dec in enumerate(decimal):
            num_char = num//dec
            num = num%dec
            output = output + num_char*roman[idx]
            
            # checking for special cases
            if idx%2 == 0:
                if num/dec >= 0.9:
                    output = output + roman[idx+2]+roman[idx]
                    num -= int(9*dec/10)
                elif 0.4 <= num/dec < 0.5:
                    output = output + roman[idx+2]+roman[idx+1]
                    num -= int(4*dec/10)
                else:
                    continue
                
        return output