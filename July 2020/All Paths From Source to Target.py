from typing import List
from copy import deepcopy

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        path = [0]
        self.dfs(path, graph)
        return self.res

    def dfs(self, path: List[int], graph: List[List[int]]) -> None:
        if path[len(path) - 1] == len(graph) - 1:
            self.res.append(deepcopy(path))
        else:
            for node in graph[path[len(path) - 1]]:
                path.append(node)
                self.dfs(path, graph)
        path.pop(len(path) - 1)

print(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
