class Solution:
    def longestPalindrome(self, s: str) -> int:
        stack = set()
        l = 0
        for c in s:
             if c in stack:
                l += 2
                stack.remove(c)
             else:
                 stack.add(c)
        if len(stack):
            l += 1
        return l


print(Solution().longestPalindrome("abccccdd"))