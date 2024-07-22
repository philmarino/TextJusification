def fullJustify(words, maxwidth):
    lines = ['']
    whichLine = 0
    spacer = ""

    #pass 1 - words into lines
    for word in words:
        if len(lines[whichLine] + spacer + word) > maxwidth:
            lines.append('')
            whichLine += 1
            spacer = ''
        lines[whichLine] = lines[whichLine] + spacer + word
        spacer = ' '
    
    #pass 2 - justification
    for whichLine in range(len(lines) - 1): #skip the last line
        howManyToAdd = 0
        lenOfWords = 0
        words = [word for word in lines[whichLine].split(' ')]
        for each in words:
            lenOfWords += len(each)

        howManyToAdd = maxwidth - lenOfWords
        added = 0
        whichWordToAddTo = 0

        while added < howManyToAdd:
            words[whichWordToAddTo] = words[whichWordToAddTo] + ' '
            added += 1
            whichWordToAddTo += 1
            if whichWordToAddTo == len(words) - 1 or len(words) == 1:
                whichWordToAddTo = 0

        lines[whichLine] = ''.join(words)

    return lines



#Example 1:
#Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
for line in fullJustify(words, maxWidth):
    print(line)
#Output:
#[
#   "This    is    an",
#   "example  of text",
#   "justification.  "
#]

#Example 2:
#Input: 
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
for line in fullJustify(words, maxWidth):
    print(line)
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:
# Input: 
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
for line in fullJustify(words, maxWidth):
    print(line)
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
