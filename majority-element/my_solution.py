class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elementDict = {}
        for num in nums:
            elementDict[num] = elementDict.get(num, 0) + 1
        
        for num in elementDict:
            if elementDict[num] > len(nums) / 2:
                return num