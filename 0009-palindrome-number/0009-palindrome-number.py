class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If the number is negative, it's not a palindrome
        if x < 0:
            return False
        
        # Store the original number
        org = x
        rev = 0
        
        # Reverse the number
        while x > 0:
            rev = rev * 10 + (x % 10)
            x = x // 10
        
        # Compare the original number with the reversed number
        return org == rev