class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # set max sub to the first value of the array
        maxSub = nums[0]
        # set curSum to 0 since there is no sum
        curSum = 0

        # loop through all nums
        for num in nums:
            # if the current sum is less than 0, we're going to disregard it.
            # there is no sense in keeping sums that are negative
            # even if a negative number positively increases, the largest sub array would be the one positive value
            # If the whole array is negative, then the max sub array is the greatest negative number
            if curSum < 0:
                curSum = 0
            # negative numbers will stay negative
            curSum += num
            # compare curr sum to the max sum
            # will find the greatest negative number and the greatest sum of a positive subarray
            maxSub = max(maxSub, curSum)
        # return maxSub
        return maxSub