import heapq
from collections import Counter,deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        vals = [-count for count in counts.values()]
        heapq.heapify(vals)
        queue = deque()
        time = 0
        while vals or queue :
            # val in queue becomes available 
            if queue and queue[0][1] < time:
                val = queue.popleft()
                if val[1] > 0:
                    heapq.heappush(vals,(val[0]-1)*(-1))
            # Pop value and add to the queue 
            elif vals:
                val = heapq.heappop(vals)
                if (val*(-1)) -1 > 0:
                    queue.append(((val*(-1)), time+n))
                time +=1
            else:
                time+=1
            
        return time
            
            

            