from dictogram import Dictogram
import random
import sys


def create_dictogram(word_string):
    '''Return dictionary of all histograms'''

    word_arr = word_string.split()
    histogram = {}

    for index in range(len(word_arr) - 1):
        current_word = word_arr[index]
        next_word = word_arr[index + 1]

        if current_word in histogram:
            histogram[current_word].add_count(next_word)
        else:
            histogram[current_word] = Dictogram([next_word])

    return histogram

def markov_chain_nth_order(word_string):
    word_arr = word_string.split()
    histogram = {}

    for index in range(len(word_string) - nth_order):
        tuple_ = tuple((text_array[i]) for i in range(index, index + nth_order))
        next_word = word_arr[index + nth_order]

        if current_tuple in dictogram_dictionary:
            dictogram_dictionary[tuple_].add_count(next_word)
        else:
            dictogram_dictionary[tuple_] = Dictogram([next_word])

    return(histogram)


def sample(dictogram):
    ''' Use the previous word in sentence array to find the inner list of next word.
    Then get a random word from that inner list'''

    word_arr = [word for word in dictogram]
    tokens = 0

    for word in word_arr:
        tokens += dictogram[word]

    random_num = random.randint(0, tokens - 1)

    # Keep track of which word has been picked by substracting frequency by 1
    for word, freq in dictogram.items():
        while freq > 0:
            if random_num > 0:
                random_num -= 1
                freq -= 1
            else:
                return word


def generate_sentence(dictogram):
    sentence_arr = ['one']

    for i in range(7):
        # Use the current word from sentence_arr as reference to find the next word
        sample_word = sample(dictogram[sentence_arr[i]])
        sentence_arr.append(sample_word)

    return ' '.join(sentence_arr)

def main():
    given_text = "one fish two fish red fish blue fish"
    # histogram = create_dictogram(given_text)
    second_order =
    sentence = generate_sentence(histogram)
    print(sentence)


if __name__ == '__main__':
    main()
