class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        max_l variable - which will store the length of the longest substring
        dict_s - store the latest occurance of the character
        start_idx - start index of the substring
        
        loop over each char in s:
            if char is in dict and start_idx of substring is <= what dictionary has:
                update the start_index
            else: (the char is new and is not in the dict)
                max(max_l, char_index - start_idx + 1)
            
            dict_s[char] = i
                
        """
        
        max_l = 0
        start_idx = 0
        dict_char = {}
        
        # acab
        
        for i in range(len(s)):
            char = s[i] # i = 3 , char = b, {a:2, c:1}, start_idx = 1
            if char in dict_char and dict_char[char]>=start_idx:
                # move start index to the character after the it occured
                start_idx = dict_char[char]+1
            else:
                max_l = max(max_l, i-start_idx+1) # max_l = 3
            dict_char[char] = i # {a:2, b:3, c:1}
        
        return max_l