from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        t = list(zip(indices, s))
        t.sort(key=lambda x : x[0])

        return "".join([x[1] for x in t])

s = "aaiougrt"
indices = [4,0,2,6,7,3,1,5]
print(Solution().restoreString(s, indices))