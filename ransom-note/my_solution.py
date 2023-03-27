class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Set Dicts
        ransomDict = {}
        magDict = {}

        for c in ransomNote:
            ransomDict[c] = ransomDict.get(c, 0) + 1

        for c in magazine:
            magDict[c] = magDict.get(c, 0) + 1

        for c in ransomDict:
            if ransomDict[c] > magDict.get(c, 0):
                return False
        
        return True