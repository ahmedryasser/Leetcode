class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_mapping = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        visited = set()
        for word in words:
            # translate
            visited.add("".join(morse_code_mapping[x] for x in word))
        return len(visited)
        
        