import math

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            k = math.ceil(math.log(num, 10)) + 1
            num = sum([ (num%(10**(i+1)) - num%(10**i))//10**i for i in range(k)])
        return num

print(Solution().addDigits(1000))