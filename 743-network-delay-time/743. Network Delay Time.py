class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v,w)) #dest, weight

        minheap = [[0, k]] #0 cost, k starting
        visit = set()
        t = 0

        while minheap:
            if len(visit) == n: #stop looking if it reaches all nodes
                return t

            w, v = heapq.heappop(minheap)
            if v in visit:
                continue
            visit.add(v)
            t = w # max of all ?

            for n2, w2 in adj[v]:
                heapq.heappush(minheap, (w + w2, n2))
            
        if n == len(visit):
            return w
        return -1