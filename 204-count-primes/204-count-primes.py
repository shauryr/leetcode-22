class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        
        '''
        Make an array of size n/2
        1. start with 2 and iterate over n checking 
        - remove the ones which mod 2 give 0; keep the ones which dont
        2. do same with 3  and keep going till n/2
        '''
        # 1 means it is prime
        # 0 means it is not prime
        numbers = [0, 0]+[1]*(n-2)
        
        for i in range(2, int(sqrt(n) + 1)):

            # set all multiples of p to 0 - they are not prime
            if numbers[i] == 1:
                for multiple in range(i*i, n, i):
                    numbers[multiple] = 0

        
        result = 0
        
        for j in numbers:
            if j:
                result+=1
                
        return result
            
        
        
        
        