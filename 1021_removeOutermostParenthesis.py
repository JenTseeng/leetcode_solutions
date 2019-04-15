class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        out = []
        open_paren = 0
        for char in S:
            if char == '(':
                if open_paren:
                    out.append(char)
                open_paren += 1
            
            elif char == ')':
                open_paren -= 1
                if open_paren:
                    out.append(char)
            else:
                out.append(char)
        
        return ''.join(out)