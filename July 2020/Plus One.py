class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        pro = False
        for i in range(len(digits) - 1, -1, -1):
            if pro:
                digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                pro = True
            else:
                pro = False
        if pro:
            digits.insert(0, 1)
        return digits


print(Solution().plusOne([9,9,9]))