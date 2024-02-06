class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqmap = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            reqmap[c].append(p)

        visit = set()
        def dfs(c):
            if c in visit:
                return False
            if reqmap[c] == []:
                return True
            
            visit.add(c)

            for p in reqmap[c]:
                if not dfs(p):
                    return False
            
            visit.remove(c)
            reqmap[c] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        