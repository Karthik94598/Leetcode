class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            x = floor(numBottles/numExchange) # 3 ,1
            res += x # 18
            n = numBottles - (numExchange * x)# 15-12=3
            numBottles = n +x #6
        return res