class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        citations.sort()
        for i in citations:
            if i<length:
                length -=1
        return length