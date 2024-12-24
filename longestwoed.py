def longest_word(sentence):
    word=sentence.split()
    return max(word,key=len)
sentence="python is best programming language"
print(longest_word(sentence))