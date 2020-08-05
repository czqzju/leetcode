import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        p = math.floor(math.log(num, 4))
        if 4 ** p == num or 4 ** (p+1) == num:
            return True
        else:
            return False

print(Solution().isPowerOfFour(5))