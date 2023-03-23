class Solution:
    def isValid(self, s: str) -> bool:
        # FILO for open bracket characters
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        # Iterate through S
        for c in s:
            # if C is in the close dict
            if c in closeToOpen:
                # detect if the top of the stack is a match to c, remove top if a match
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    # detect mismatch and return false
                    return False
            else:
                # only append open brackets
                stack.append(c)

        # returns True if stack is empty, returns False otherwise
        return True if not stack else False