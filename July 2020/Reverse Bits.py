import numpy as np
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res <<= 1
            if n & 1 == 1: res += 1
            n >>= 1
        return res

print(Solution().reverseBits(0b00000010100101000001111010011100))