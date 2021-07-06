def no_dups(s):
    # Your code here
    #if there's nothing in the string just return the string
    if len(s) == 0:
        return s
    words = s.split()
    newWords = []
    newS = " "

    # print(words[0])

    for i in words:
        if i not in newWords:
            newWords.append(i)
    
    return newS.join(newWords)
    


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))