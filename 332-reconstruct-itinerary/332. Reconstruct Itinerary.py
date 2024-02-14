class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #paths = defaultdict(list)
        paths = {f:[] for f,t in tickets}


        

        for f,t in tickets:
            paths[f].append(t)

        for key in paths:
            paths[key].sort()


        res = []

        def dfs(src):
            if src in paths:
                temp = paths[src][:]
                while temp:
                    dest = temp[0]
                    paths[src].pop(0)
                    dfs(dest)
                    temp = paths[src][:]
            res.append(src)
            
        
        dfs("JFK")
        res.reverse()
        return res

            

        