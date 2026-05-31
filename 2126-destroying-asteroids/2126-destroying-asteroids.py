class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for astroid in asteroids:
            if astroid > mass:
                return False
            mass += astroid
        return True