class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                       ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                       "...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        for word in words:
            morse_chars = [morse_alpha[ord(char)-ord('a')] for char in word]
            transformations.add(''.join(morse_chars))
        
        # one liner solution w/ set comprehension
        # transformations = {''.join([morse_alpha[ord(char)-ord('a')] for char in word]) 
        # for word in words}

        return len(transformations)