class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dist(a,b,c,d):
            return (a - c)**2 + (b - d)**2
        
        adj = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]
                distance = dist(x1,y1,x2,y2)
                if distance <= r1**2:
                    adj[i].append(j)
                if distance <= r2**2:
                    adj[j].append(i)
                    
        def dfs(i, seen):
            if i in seen:
                return
            seen.add(i)
            for j in adj[i]:
                dfs(j, seen)
        
        res = 0
        for i  in range(len(bombs)):
            seen = set()
            dfs(i,seen)
            res = max(res,len(seen))
        return res
                