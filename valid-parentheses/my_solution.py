class Solution:
    def isValid(self, s: str) -> bool:
        # Need stack because brackets need to be closed in a Last In First Out
        charStack = []
        # Loop through c characters
        for c in s:
            # Case 1: bracket is an open bracket - append to stack
            if c == '(' or c == '{' or c == '[':
                charStack.append(c)
            else:
                # Case 2: bracket is a closing bracket with no bracket to close in the stack
                if len(charStack) == 0:
                    return False
                # Pop most recent
                lastChar = charStack.pop()
                #  Case 3: Most recent closing bracket doesn't sync up with an open bracket
                if (c == ')' and lastChar != '(') or (c == '}' and lastChar != '{') or (c == ']' and lastChar != '['):
                    return False
        # Return True if all open brackets have been accomidated for
        return len(charStack) == 0