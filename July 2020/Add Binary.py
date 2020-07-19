class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(map(int, iter(a)))
        b = list(map(int, iter(b)))
        res = []
        added = 0
        while len(a) or len(b) or added:
            curA = 0
            curB = 0
            if len(a): curA = a.pop(len(a) - 1)
            if len(b): curB = b.pop(len(b) - 1)
            curSum = curA + curB + added
            if curSum == 3:
                added = 1
                res.insert(0, 1)
            elif curSum == 2:
                added = 1
                res.insert(0, 0)
            else:
                added = 0
                res.insert(0, curSum)
        return "".join(map(str, res))




print(Solution().addBinary("11", "1"))