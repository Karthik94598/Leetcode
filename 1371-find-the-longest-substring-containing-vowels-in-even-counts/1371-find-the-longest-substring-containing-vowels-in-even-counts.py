class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Initialize a dictionary to store the first occurrence of each bitmask
        mask_to_index = {0: -1}  # Bitmask 0 means all vowels have even counts
        mask = 0  # Start with all vowels having even counts
        max_len = 0
        
        # Map each vowel to its respective bit position in the bitmask
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # Traverse the string
        for i, char in enumerate(s):
            # If the character is a vowel, update the bitmask
            if char in vowel_to_bit:
                # Flip the respective bit for the vowel
                mask ^= (1 << vowel_to_bit[char])
            
            # If this bitmask has been seen before, calculate the length of the substring
            if mask in mask_to_index:
                max_len = max(max_len, i - mask_to_index[mask])
            else:
                # Otherwise, store the first occurrence of this bitmask
                mask_to_index[mask] = i
        
        return max_len
