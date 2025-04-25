from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        left = 0
        s1_dict = Counter(s1)
        s2_dict = Counter(s2[:s1_length])
        for right in range(s1_length,len(s2)):
            if s1_dict == s2_dict:
                return True
            else:
                if s2_dict[s2[left]] > 0 :
                    s2_dict[s2[left]] -=1 
                else:
                    del s2_dict[s2[left]]
                s2_dict[s2[right]] +=1
                left+=1

        return s1_dict == s2_dict


            

            