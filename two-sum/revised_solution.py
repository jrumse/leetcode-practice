class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Num Table
        numTable = {}
        # Iterate through nums
        for i, num in enumerate(nums):
            # First Check
            if (numTable.get(target - num, -1)) >= 0:
                return [i, numTable.get(target - num)]
            
            numTable[num] = i