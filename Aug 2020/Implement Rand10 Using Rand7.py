# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        r = 0

        while r == 0:
            r1 = rand7()
            r2 = rand7()

            if r1 == 1:
                if r2 < 4:
                    r = 1
                elif r2 < 7:
                    r = 2

            elif r1 == 2:
                if r2 < 4:
                    r = 3
                elif r2 < 7:
                    r = 4

            elif r1 == 3:
                if r2 < 4:
                    r = 5
                elif r2 < 7:
                    r = 6

            elif r1 == 4:
                if r2 < 4:
                    r = 7
                elif r2 < 7:
                    r = 8

            elif r1 == 5:
                if r2 < 4:
                    r = 9
                elif r2 < 7:
                    r = 10

        return r
