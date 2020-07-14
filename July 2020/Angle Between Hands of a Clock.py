class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angleHour = (hour * 30 + minutes * 30.0 / 60) % 360
        angleMinutes = minutes * 6
        diff = abs(angleHour - angleMinutes)
        if diff > 180: diff = 360 - diff

        return diff

print(Solution().angleClock(3, 15))