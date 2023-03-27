class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # set res string and default carry
        resString = ""
        carry = 0

        # reverse strings a and b so we can evaluate the back first
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            # Calculate value for the first digit
            # if i is exceeding len of a string, the digit will default to 0
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            # total is equal to the addition of both digits plus a carry
            total = digitA + digitB + carry
            # modulate by 2 to determine if digit is 0 or 1
            # append the res string to the new digit, building left
            resString = str(total % 2) + resString
            # calculate the carry in case modulo doesn't account for it
            carry = total // 2
        
        # by this point if a carry is 1, append the res string to it
        if carry:
            return str(carry) + resString
        return resString