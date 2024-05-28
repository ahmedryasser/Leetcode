class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]*(len(gain)+1)
        for index in range(1,len(gain)+1):
            altitude[index] = altitude[index-1] + gain[index-1]
        return max(altitude)
            
        