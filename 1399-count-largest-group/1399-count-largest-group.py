class Solution:
    def countLargestGroup(self, n: int) -> int:
        numbers = {}
        i = 1
        while i <= n:
            digits = list(str(i))
            digit_sum = sum(int(n) for n in digits)
            numbers[digit_sum] = numbers.get(digit_sum,0)+1
            i+=1
        biggest = max(numbers.values())
        count = 0
        for number,occur in numbers.items():
            if occur == biggest:
                count+=1
        return count