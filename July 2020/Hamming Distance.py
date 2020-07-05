class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = list(bin(x))[2:]
        y = list(bin(y))[2:]
        if len(x) > len(y):
            tmp = ['0'] * (len(x) - len(y))
            tmp.extend(y)
            y = tmp
        elif len(x) < len(y):
            tmp = ['0'] * (len(y) - len(x))
            tmp.extend(x)
            x = tmp
        res = map(lambda a, b: a!=b, x, y)
        return [i for i in res].count(True)

print(Solution().hammingDistance(40, 100))