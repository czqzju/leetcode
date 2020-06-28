import bisect
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        paths = dict()

        for s, e in tickets:
            if(s not in paths):
                paths[s] = [e]
            else:
                bisect.insort_left(paths[s], e)


        res = []
        st = ["JFK"]
        while(len(st)):
            pre = st[-1]
            if(pre not in paths or not len(paths[pre])):
                res.insert(0, pre)
                st.pop(-1)
            else:
                st.append(paths[pre][0])
                paths[pre].pop(0)
        return res



print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))