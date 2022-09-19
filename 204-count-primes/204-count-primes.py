class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        
        '''
        make a flag array of size n
        mark default values as 1 - assume everything is prime
        
        iterate from 2 to end:
            if that number is prime then:
                multiples of the prime number starting with p*p -> because all the numbers below that would have been covered by the lower prime number :  all numbers can be shown as a factor of prime numbers
                mark all these as not prime
                
        return the sum of the flag array
        
        '''
        # 1 means it is prime
        # 0 means it is not prime
        numbers = [0, 0]+[1]*(n-2)
        
        for i in range(2, int(sqrt(n) + 1)):

            # set all multiples of p to 0 - they are not prime
            if numbers[i] != 0: # if this number has been marked as prime already then only do this.
                for multiple in range(i*i, n, i):
                    numbers[multiple] = 0

        
        result = 0
        
        for j in numbers:
            if j:
                result+=1
                
        return result
            
        
        
        
        