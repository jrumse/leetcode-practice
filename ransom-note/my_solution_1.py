class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Sort the lists O(nlogn)
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        # Return if true
        if ransomNote == magazine:
            return True

        mPointer = 0

        while ransomNote:
            # If we've iterated through the whole magazine
            if mPointer >= len(magazine):
                return False

            if ransomNote[0] == magazine[mPointer]:
                ransomNote.pop(0)
            
            mPointer += 1

        return True