class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        using a stack with (value, count) tuple
        if count ==k then pop the stack
        
        '''
        
        stack = []
        
        for i in s:
            if stack and i==stack[-1][0] :
                stack[-1][1]+=1
            else:
                stack.append([i, 1])
                
            if stack[-1][1]==k:
                stack.pop()
            
        result = ''
        for char, count in stack:
            result += char*count
        
        return result
        
        