"""count how many times each space-separated word occurs"""


def word_count(file=open("test.txt")):
    """Open .txt file and add contents to a dictionary, then count how many times each word appears."""

    number_of_words = {}

    for line in file:
        #each_word = line.split()
        for each_word in line.split():
            if each_word not in number_of_words:
                number_of_words[each_word] = 1
            else:
                number_of_words[each_word] += 1
            #line.pop(each_word)

            #print(each_word)

    print(number_of_words)


word_count()
