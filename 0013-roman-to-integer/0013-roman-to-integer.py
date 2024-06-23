class Solution:
    def romanToInt(self, s: str) -> int:
        ri={'I':1 , 'V':5 , 'X':10 ,'L':50 , 'C' :100 , 'D': 500 ,'M':1000}
        n=len(s)
        num =0
        for i in range (n):
            if i+1 < n and ri[s[i]] < ri[s[i+1]]:
                num -= ri[s[i]]
            else:
                num += ri[s[i]]
        return num
        