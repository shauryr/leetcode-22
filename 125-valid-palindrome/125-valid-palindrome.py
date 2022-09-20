class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1
        
        while L < R:
            if s[L].isalnum() and s[R].isalnum():
                if s[L].lower()==s[R].lower():
                    L+=1
                    R-=1
                else:
                    return False
            else:
                # increment if char is not alphnumeric
                if not s[L].isalnum():
                    L+=1
                if not s[R].isalnum():
                    R-=1
        
        return True