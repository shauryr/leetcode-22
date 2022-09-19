class Solution:
    def isValid(self, s: str) -> bool:
        
        """
        create a map of reverse paranthesis(P)
        create a stack
        iterate over s:
            if encountered P is in the map:
                pop from the stack
                if popped element is not equal to map value
                return false
            else:
                append(stack)
        
        """
        
        map_para = {
            ']':'[',
            ')' : '(',
            '}' : '{'
        }
        
        stack = []
        
        for p in s:
            if p in map_para and stack:
                p_rev = stack.pop()
                if p_rev != map_para[p]:
                    return False
            else:
                stack.append(p)
        
        return not stack
                