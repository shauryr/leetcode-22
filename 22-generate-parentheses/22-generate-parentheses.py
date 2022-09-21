class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final_array = []
        
    
    
        def recursive(open_n , close_n, string, final_array, n):

            if open_n==n and close_n==n:
                final_array.append(string)
                return

            if open_n < n:
                recursive(open_n + 1, close_n, string+"(", final_array, n)

            if close_n < open_n:
                recursive(open_n, close_n + 1, string+")", final_array, n)
    
    
        recursive(0, 0, "",final_array,n)
        return final_array