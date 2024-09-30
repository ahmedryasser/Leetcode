class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        routes = {}
        for path in paths:
            routes[path[0]] = path[1]
        start = paths[0][1]
        while start in routes:
            start = routes[start] 
        return start