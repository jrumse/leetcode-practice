class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set left and right indexes
        l, r = 0, len(s) - 1

        # left increases from 0, r decreases from len
        while r > l:
            # iterate up until we find an alpha numeric character
            while not self.alphaNum(s[l]) and l < r:
                l += 1
    
            # iterate down until we find an alpha numeric character
            while not self.alphaNum(s[r]) and r > l:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        
        return True

    # This is only necessary if the interviewer won't let you use built ins to determine if a char is alpha numeric
    # It's a good lesson in ascii however
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))