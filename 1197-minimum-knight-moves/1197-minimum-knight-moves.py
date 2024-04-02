class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Directions a knight can move
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                      (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        # Initialize queue and visited set. Each element in queue: (x, y, count)
        queue = [(0, 0, 0)]
        visited = {(0, 0)}
        
        while queue:
            current_x, current_y, count = queue.pop(0)
            # If target is reached, return the count of moves
            if current_x == x and current_y == y:
                return count
            
            # Explore all possible moves from the current position
            for dx, dy in directions:
                next_x, next_y = current_x + dx, current_y + dy
                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, count + 1))