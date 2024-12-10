class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        counter = 0
        numwords = 0
        curr = []
        res = []

        i = 0
        while i < len(words):
            word = words[i]
            if counter + len(word) + numwords > maxWidth:
                chars = sum(len(w) for w in curr)
                spacearr = []
                if numwords > 1:
                    q, r = divmod(maxWidth - chars, numwords - 1)
                    spacearr = [" " * q for _ in range(numwords - 1)]
                    for j in range(r):
                        spacearr[j] += " "
                    currSpaced = []
                    for idx in range(len(curr)):
                        currSpaced.append(curr[idx])
                        if idx < len(spacearr):
                            currSpaced.append(spacearr[idx])
                    res.append("".join(currSpaced))
                else:
                    res.append(curr[0].ljust(maxWidth))
                curr = []
                counter = 0
                numwords = 0
                i -= 1  # Re-process the current word
            else:
                curr.append(word)
                counter += len(word)
                numwords += 1
            i += 1

        # Handle the last line
        last_line = " ".join(curr).ljust(maxWidth)
        res.append(last_line)

        return res

        