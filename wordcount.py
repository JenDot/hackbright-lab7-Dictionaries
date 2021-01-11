"""count how many times each space-separated word occurs"""
text_file = open('test.txt')


def word_count(text_file):
    # create empty dictionary
    words = {}

    # for word in text_file:
    #     #print(word)
    #     # line.rstrip().split(' ', -1)
    #     words[word] = words.get(word, 0) + 1
    #     return words

    for line in text_file:
        new_line = line.rstrip().split()
        for word in new_line:
            #a = dict(one=1, two=2, three=3)
            #b = {'one': 1, 'two': 2, 'three': 3}
            words[word] = {word: 1}
            #words[word] = words.get(word, 0) + 1
            #print(f'{word} {words[word]}')
            #print(type(words))
    #return f'{word} {words[word]}'


print(word_count(text_file))

#https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
