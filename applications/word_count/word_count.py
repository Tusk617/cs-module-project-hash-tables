import re
def word_count(s):
    # Your code here
    cache = {}
    # print(newS)
    # newString = re.sub('[^a-zA-z/W+]', ' ', s)
    newString = s.split()
    print(newString)
    for word in newString:
        word = word.isalpha()
    
    for word in newString:
        word = word.lower()
        cache[word] = newString.count(word)
    return cache
    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))