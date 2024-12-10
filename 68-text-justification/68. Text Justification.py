class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        counter = 0
        numwords = 0
        curr = []
        res = []

        i = 0
        while i < len(words):
            word = words[i]
            if counter + len(word) + numwords > maxWidth:  # Fixed condition to include spaces
                chars = 0
                spacearr = []
                for word in curr:
                    chars += len(word)
                
                if numwords > 1:
                    q, r = divmod((maxWidth - chars), numwords - 1)
                    spacearr = [q * " "] * (numwords - 1)
                    
                    j = 0
                    while r > 0:
                        spacearr[j] += " "
                        r -= 1
                        j += 1

                    currSpaced = []
                    for idx in range(len(curr)):  # Fixed merging of words and spaces
                        currSpaced.append(curr[idx])
                        if idx < len(spacearr):
                            currSpaced.append(spacearr[idx])
                else:
                    numspaces = maxWidth - len(curr[0])
                    currSpaced = [curr[0] + " " * numspaces]

                res.append(currSpaced)
                curr = []
                counter = 0
                numwords = 0
                i -= 1  # Re-process the current word
            else:
                curr.append(word)
                counter += len(word)
                numwords += 1
            i += 1

        # Handle the last line (Left-align the last line)
        last_line = " ".join(curr).ljust(maxWidth)  # Fixed to left-align and pad spaces
        res.append(last_line)

        return ["".join(x) for x in res]
