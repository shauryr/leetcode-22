class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping_braces = {
            ')' : '(',
            "}" : "{",
            "]" : "["
        }
        
        for c in s:
            if c in mapping_braces and len(stack)!=0 :
                top = stack.pop()
                if top != mapping_braces[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack