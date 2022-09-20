class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverse(num):
            _cache = num
            rev = 0
            while num>0:
                n = num%10
                rev = rev*10 + n
                num = num//10
            return rev==_cache
        
        return reverse(x)