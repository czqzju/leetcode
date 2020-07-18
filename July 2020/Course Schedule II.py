from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = { x for x in range(numCourses) }
        edges = dict()
        cntInDegree = dict()
        for prerequisity in prerequisites:
            if prerequisity[0] in courses:
                courses.remove(prerequisity[0])

            if prerequisity[1] not in edges:
                edges[prerequisity[1]] = []
            if prerequisity[0] not in cntInDegree:
                cntInDegree[prerequisity[0]] = 0
            edges[prerequisity[1]].append(prerequisity[0])
            cntInDegree[prerequisity[0]] += 1

        if len(courses) < 1: return []


        res = []
        parents = list(courses)
        while len(parents):
            parent = parents.pop(0)
            res.append(parent)
            if parent in edges:
                for c in edges.pop(parent):
                    if c in cntInDegree:
                        cntInDegree[c] -= 1
                        if cntInDegree[c] == 0:
                            cntInDegree.pop(c)
                            parents.append(c)
        if len(res) == numCourses:
            return res
        else:
            return []

print(Solution().findOrder(3, [[0,1],[0,2],[1,2]]))











