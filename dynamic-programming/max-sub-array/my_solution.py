class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # take either the value at the index
        # OR
        # value at the current index + max sum of the prev index
        # Using Kadane's Algorithm for memoizing maximum sub arrays

        # Value List is where we'll store
        valueList = []
        # constant comparisons to the masx
        currMax = nums[0]

        # loop through the nums
        for (i, num) in enumerate(nums):
            # base case: don't do anyting
            if i == 0:
                valueList.append(num)
            else:
                # index val + prev max
                newVal = num + valueList[i - 1]
                # determine if this newVal is a new maximum
                currMax = max(currMax, max(num, newVal))
                # append the new value
                valueList.append(max(num, newVal))
    
        return currMax