class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_mapping = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        visited = set()
        for word in words:
            # translate
            string = ""
            for letter in word:
                string += morse_code_mapping[letter]
            visited.add(string)
        return len(visited)
            