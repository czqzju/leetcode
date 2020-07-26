class Solution:
    def minFlips(self, target: str) -> int:
        cnt = 0
        for i in range(len(target)):
            if target[i] == '0':
                if cnt % 2 == 1:
                    cnt += 1
            else:
                if cnt % 2 == 0:
                    cnt += 1
        return cnt

print(Solution().minFlips("001011101"))