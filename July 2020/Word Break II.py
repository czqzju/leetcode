from typing import List, Tuple
from itertools import combinations

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        s1 = set(s)
        s2 = set("".join(wordDict))
        if len(s1.difference(s2)):
            return []
        self.res = []
        self.startLetter = dict()
        for word in wordDict:
            if not word[0] in self.startLetter:
                self.startLetter[word[0]] = []
            self.startLetter[word[0]].append(word)
        self.findDFS([], s)

        return self.res

    def findDFS(self, words: List, s: str):
        if not len(s):
            self.res.append(" ".join(words))
            return
        if len(s) and s[0] in self.startLetter:
            for word in self.startLetter[s[0]]:
                if len(s) >= len(word) and word == s[0: len(word)]:
                    words.append(word)
                    self.findDFS(words, s[len(word):])
                    words.pop(len(words) - 1)



print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))


