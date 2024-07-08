class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # The position of the winner (0-indexed)
        
        for i in range(1, n + 1):
            winner = (winner + k) % i
        
        # Convert the 0-indexed position to 1-indexed
        return winner + 1
