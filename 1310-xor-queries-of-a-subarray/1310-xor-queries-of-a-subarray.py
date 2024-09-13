class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Create the prefix_xor array
        prefix_xor = [0] * (len(arr) + 1)
        
        for i in range(1, len(arr) + 1):
            # prefix_xor[i] contains XOR of all elements from arr[0] to arr[i-1]
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]
        
        # Step 2: Answer each query using the prefix_xor array
        result = []
        for left, right in queries:
            # XOR from left to right is calculated as:
            # prefix_xor[right + 1] ^ prefix_xor[left]
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])
        
        return result
