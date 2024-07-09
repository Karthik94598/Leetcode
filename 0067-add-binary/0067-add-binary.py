class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total_sum = carry
            if i >= 0:
                total_sum += int(a[i])
                i -= 1
            if j >= 0:
                total_sum += int(b[j])
                j -= 1

            carry = total_sum // 2
            result.append(str(total_sum % 2))

        return ''.join(reversed(result))