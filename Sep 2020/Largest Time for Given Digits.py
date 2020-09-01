from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        self.curMaxTime = []
        for per in permutations(A):
            hour = "".join(map(str, per[:2]))
            minute = "".join(map(str, per[2:]))

            if self.isValidTime(hour, minute):
                self.updateMaxTime(hour, minute)

        if len(self.curMaxTime):
            return ":".join(self.curMaxTime)
        else:
            return ""

    def updateMaxTime(self, hour: str, minute: str) -> None:
        if len(self.curMaxTime):
            if int(self.curMaxTime[0]) < int(hour):
                self.curMaxTime[0] = hour
                self.curMaxTime[1] = minute
            elif int(self.curMaxTime[0]) > int(hour):
                return
            else:
                if int(self.curMaxTime[1]) < int(minute):
                    self.curMaxTime[0] = hour
                    self.curMaxTime[1] = minute
        else:
            self.curMaxTime.append(hour)
            self.curMaxTime.append(minute)

    def isValidTime(self, hour: str, minute: str) -> bool:
        if int(hour) < 24 and int(minute) < 60:
            return True
        else:
            return False



a = [5,5,5,5]
print(Solution().largestTimeFromDigits(a))