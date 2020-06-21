class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        counts = []
        digits = []
        curCnt = 1
        for i in range(1, n + 1):
            curCnt = curCnt * (i - 1) if (i > 1) else curCnt * i
            counts.append(curCnt)
            digits.append(i)
        res = 0
        while (len(digits)):
            if (k == 0):
                res = res * 10 + digits.pop(-1)
                continue
            if (k == 1):
                res = res * 10 + digits.pop(0)
                continue
            index, remain = divmod(k, counts[n - 1])
            if (remain == 0):
                res = res * 10 + digits.pop(index - 1 if index > 0 else index)
                while (len(digits)):
                    res = res * 10 + digits.pop(-1)
            else:
                res = res * 10 + digits.pop(index)
                k = remain
            n -= 1

        return str(res)

print(Solution().getPermutation(4, 9))