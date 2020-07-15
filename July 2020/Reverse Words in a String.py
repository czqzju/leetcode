import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = re.findall(r'[^\s]+', s)
        res = reversed(res)
        return " ".join(res)

print(Solution().reverseWords("  hello   world!  "))