from collections import defaultdict
import heapq
class TimeMap:

    def __init__(self):
        self.people = {}
        self.recent = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.people:
            self.people[key] = {timestamp: value}  
            self.recent[key] = []
            heapq.heapify(self.recent[key])
        else: 
            self.people[key][timestamp] = value
        
        heapq.heappush(self.recent[key], timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.people and timestamp in self.people[key]:
            return self.people[key][timestamp] 
        elif key in self.recent:
            for time in reversed(self.recent[key]):
                if time <timestamp:
                    return self.people[key][time]
            
            return ""
        else:
            return ""
        
