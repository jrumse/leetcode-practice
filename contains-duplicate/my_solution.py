class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsTable = {}

        for num in nums:
            numsTable[num] = numsTable.get(num, 0) +1
            if numsTable[num] > 1: return True
        
        return False