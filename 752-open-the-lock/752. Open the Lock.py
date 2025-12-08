import queue
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # BFS Queue
        # DFS Stack
        if "0000" in deadends:
            return -1

        q = queue.Queue()
        visited = set()
        q.put(["0000", 0])   
        visited.add("0000")

        while q.qsize() > 0:
            t = q.get()
            if t[0] == target:
                return t[1]

            for i in range(4):
                current = int(t[0][i])
                current += 1
                current %= 10
                next_string = t[0][:i] + str(current) + t[0][i+1:]
                if next_string not in visited and next_string not in deadends:
                    q.put([next_string, t[1] + 1])
                    visited.add(next_string)
                
                current = int(t[0][i])
                current -= 1
                current = (current + 10)%10

                next_string = t[0][:i] + str(current) + t[0][i+1:]
                if next_string not in visited and next_string not in deadends:
                    q.put([next_string, t[1] + 1])
                    visited.add(next_string)

        return -1

            