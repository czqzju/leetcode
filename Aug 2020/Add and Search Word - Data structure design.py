class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if not len(word): return

        curNode = self.root
        for i in range(len(word)):
            if not word[i] in curNode: curNode[word[i]] = dict()
            curNode = curNode[word[i]]
        if not -1 in curNode: curNode[-1] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not len(word): return False
        curNodes = [self.root]
        for i in range(len(word)):
            children = []
            if not len(curNodes): return False
            for node in curNodes:
                if word[i] == '.':
                    for k in node.keys():
                        if k == -1: continue
                        children.append(node[k])
                else:
                    if word[i] in node:
                        children.append(node[word[i]])
            curNodes = children
        if not len(curNodes): return False
        for node in curNodes:
            if -1 in node:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
ops = ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]

paras = [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]

obj = None
res = []
for i in range(len(ops)):
    if ops[i] == "WordDictionary":
        obj = WordDictionary()
        res.append("null")
    elif ops[i] == "addWord":
        obj.addWord(paras[i][0])
        res.append("null")
    else:
        res.append(obj.search(paras[i][0]))

print(res)