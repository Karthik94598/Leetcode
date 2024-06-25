class Solution:
    def isValid(self, s: str) -> bool:
        d={
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if stack == [] or stack.pop() != d[i]:
                    return False
            else:
                return False
        return len(stack) == 0
                
        