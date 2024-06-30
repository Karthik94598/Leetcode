class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.strip().split()
        return(len(x[-1]))