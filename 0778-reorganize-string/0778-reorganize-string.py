class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s

        counts = {l:0 for l in s}

        for letter in s:
            counts[letter] +=1
        
        if max(counts.values()) <= ceil(len(s)/2):
            letters = []
            while max(counts.values()) >0 and len(counts.values())>1:
                maximum = max(counts.values())
                minimum = min(counts.values())
                if maximum == minimum:
                    for letter,count in counts.items():
                        letters.append(letter)
                        counts[letter] -=1
                        
                    continue

                else:
                    maxVal = [c for c in counts if counts[c] == maximum][0]
                    minVal = [c for c in counts if counts[c] == minimum][0]
                    letters.append(maxVal)
                    letters.append(minVal)
                    counts[maxVal] -=1
                    counts[minVal] -=1
                    if counts[minVal] == 0:
                        del counts[minVal]
                        if counts[maxVal] == 0:
                            del counts[maxVal]
            return "".join(letters) if max(counts.values()) == 0 else "".join(letters + [maxVal])
        else:
            return ""