class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Base case: 1 element left and it's not the target
        if len(nums) == 1 and nums[0] != target:
            return -1

        # take the midpoint
        midpoint = len(nums) // 2

        # Check if midpoint value == target
        if nums[midpoint] == target:
            # Element found, return the midpoint
            return midpoint
        elif target < nums[midpoint]:
            # Midpoint addition not required to track first half
            return self.search(nums[:midpoint], target)
        else:
            # midpoint addition required to track the second half indexes
            idx = self.search(nums[midpoint:], target)
            # need to continue to return back -1 if the element is not found
            if idx != -1:
                return midpoint + idx
            return idx
        

# How many times can we divide by 2? that would be log_2(n)