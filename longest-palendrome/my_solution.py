class Solution:
    def longestPalindrome(self, s: str) -> int:

        palDict = {}
        duplicateCounter = 0

        # Populate pal dict into counts
        for c in s:
            palDict[c] = palDict.get(c, 0) + 1
            # a duplicate has been discovered
            if palDict[c] % 2 == 0:
                duplicateCounter += 2
                palDict[c] = 0
        
        for c in s:
            if palDict[c] == 1:
                return duplicateCounter + 1
        
        return duplicateCounter