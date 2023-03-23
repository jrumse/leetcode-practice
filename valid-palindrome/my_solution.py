class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set left and right indexes
        l, r = 0, len(s) - 1

        # left increases from 0, r decreases from len
        while r > l:
            # iterate up until we find an alpha numeric character
            while not s[l].isalnum() and l < r:
                l += 1
    
            # iterate down until we find an alpha numeric character
            while not s[r].isalnum() and r >= l:
                r -= 1

            if not r > l:
                break
            
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        
        return True