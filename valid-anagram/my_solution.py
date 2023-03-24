class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Declare Dicts
        sDict, tDict = {}, {}
        # For charaters in string S
        for c in s:
            # Iterate appearance count starting at 0
            sDict[c] = sDict.get(c, 0) + 1
        # For characters of string t
        for c in t:
            # Iterate appearance count starting at 0
            tDict[c] = tDict.get(c, 0) + 1
        # Return if the dicts are equal (this means its an anagram)
        return sDict == tDict
    
# You can also put s and t in sorted order and return s == t
# might be considered cheating, also isn't the most efficient due to the sort algorithm not running consistently at O(n)