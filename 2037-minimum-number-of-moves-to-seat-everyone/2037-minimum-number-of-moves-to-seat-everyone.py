class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        diff =0
        for n in range(len(seats)):
            diff+= abs(seats[n]-students[n])
        return diff