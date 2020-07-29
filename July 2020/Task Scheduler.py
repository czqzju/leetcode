from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        arr = []
        for k,v in cnt.items():
            arr.append([k, v])
        arr.sort(key=lambda x : x[1])
        index = len(arr) - 1
        mx = arr[index][1]
        while index>=0 and arr[index][1] == mx : index -= 1
        return max(len(tasks), (mx-1)*(n+1) + len(arr) - 1 -index)

print(Solution().leastInterval(["A","A","A","B","B","B"], 2))