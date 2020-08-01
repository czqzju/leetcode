class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word or word.capitalize() == word or word.lower() == word:
           return True
        else:
            return False

print(Solution().detectCapitalUse("FlaG"))