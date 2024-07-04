class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert list of digits to a single integer
        a = int(''.join(str(i) for i in digits))
        # Increment the integer by one
        a += 1
        # Convert the integer back to a list of digits
        digits = [int(i) for i in str(a)]
        return digits