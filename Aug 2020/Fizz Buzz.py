from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        self.res = []
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                self.res.append("FizzBuzz")
            elif num % 3 == 0:
                self.res.append("Fizz")
            elif num % 5 == 0:
                self.res.append("Buzz")
            else:
                self.res.append(str(num))

        return self.res


print(Solution().fizzBuzz(15))