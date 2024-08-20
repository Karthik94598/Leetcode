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
# Iteration Over Each Character:

# Index 0 (M):

# Value is 1000.
# Next numeral is C (value 100).
# Since 1000 > 100, add 1000 to num. Now, num = 1000.
# Index 1 (C):

# Value is 100.
# Next numeral is M (value 1000).
# Since 100 < 1000, subtract 100 from num. Now, num = 900.
# Index 2 (M):

# Value is 1000.
# Next numeral is X (value 10).
# Since 1000 > 10, add 1000 to num. Now, num = 1900.
# Index 3 (X):

# Value is 10.
# Next numeral is C (value 100).
# Since 10 < 100, subtract 10 from num. Now, num = 1890.
# Index 4 (C):

# Value is 100.
# Next numeral is I (value 1).
# Since 100 > 1, add 100 to num. Now, num = 1990.
# Index 5 (I):

# Value is 1.
# Next numeral is V (value 5).
# Since 1 < 5, subtract 1 from num. Now, num = 1989.
# Index 6 (V):

# Value is 5.
# There’s no next numeral, so add 5 to num. Now, num = 1994.
