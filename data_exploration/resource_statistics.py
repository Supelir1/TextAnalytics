from collections import Counter

import numpy as np
import spacy
from matplotlib import pyplot as plt

nlp = spacy.load('de_core_news_md')


def plotting_png(most_freq_words, name, save_image):
    list_g = []
    list_x = []
    list_y = []

    i = 0
    for word in most_freq_words:
        list_g.insert(i, word)
        i += 1

    j = 0
    for (x, y) in list_g:
        list_x.insert(i, x)
        list_y.insert(i, y)
        j += 1

    x = np.arange(50)
    plt.xticks(x, list_x, rotation='vertical')
    plt.bar(list_x, list_y, color='blue')
    if save_image:
        plt.savefig(name + '.png')
        print("Plot saved as " + name + ".png")
    plt.show()


def get_stats(name, save_image=False):
    print("Getting statistics...")
    with open('../resources/' + name + '.txt', encoding='utf-8', errors='ignore') as f:
        file = " ".join(token.rstrip() for token in f)
    print("Processing file...")
    text = nlp(file)
    print("Removing stopwords...")
    words = [token.lemma_ for token in text if not token.is_stop and
             not token.is_punct and
             not token.is_space and
             token.pos_ != 'NUM' and
             not token.is_upper]
    print("Counting words...")
    word_freq = Counter(words)
    most_freq_nouns = word_freq.most_common(50)
    print("Plotting graph...")
    plotting_png(most_freq_nouns, 'graph' + name, save_image)


if __name__ == '__main__':
    select = '''
    Which party would you like to review?
    0 - AfD
    1 - CDU
    2 - FDP
    3 - GRÜNE
    4 - LINKE
    5 - SPD \n
    Choose with the corresponding number: 
    '''
    selection = input(select)

    PARTY_NAME = ["AFD", "CDU", "FDP", "GRUENE", "LINKE", "SPD"]
    if selection in ['0', '1', '2', '3', '4', '5']:
        get_stats(PARTY_NAME[int(selection)])
