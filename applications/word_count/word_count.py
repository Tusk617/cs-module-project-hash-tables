import re
def word_count(s):
    # Your code here
    cache = {}
    # newString = s.split()
    newS = re.sub(r'[^a-zA-Z\W]', ' ', s)
    newString = newS.split(' ')
    print(newS)
    # print(newString)
    # ignoredChars = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '*', '{', '}', '^', '&', ']', '[']
    # print(newString)
    for word in newString:
        word = word.lower()
        cache[word] = newS.count(word)
    return cache
    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))