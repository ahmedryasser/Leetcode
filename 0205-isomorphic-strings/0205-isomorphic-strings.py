class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        
        for l1,l2 in zip(s,t) :
            ls = list(mapping.values())
            if l1 not in mapping:
                mapping[l1] = l2
            else:
                if mapping[l1] != l2:
                    return False
        return len(set(mapping.keys())) == len(set(mapping.values()))