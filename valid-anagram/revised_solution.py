class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # It's impossible to have an anagram of two different length strings
        if len(s) != len(t):
            return False
        
        # Declare Dicts
        sCount, tCount = {}, {}

        # loop thru S
        # We can do this for both S and T bc they are the same length
        for i in range(len(s)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            tCount[t[i]] = tCount.get(t[i], 0) + 1
        
        return sCount == tCount
    
# If you can't return sCount == tCount, you can loop through sCount's keys and compare their value's to tCount's matching keys
# then do the same for tCount matching sCount keys
# If there is a discrepency, return false
# Else, return true

# You can also put s and t in sorted order and return s == t
# might be considered cheating, also isn't the most efficient due to the sort algorithm not running consistently at O(n)