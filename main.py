from collections import Counter

import numpy as np
import spacy
from matplotlib import pyplot as plt

if __name__ == '__main__':

    # TODO: md oder lg?
    nlp = spacy.load('de_core_news_md')
    print(nlp.pipe_names)

    # mit Methode pipe(<datei>) und Path optimierbar(siehe Zeile 180)
    with open('Gruene.txt', encoding='utf-8', errors='ignore') as g:
        dateiGruene = " ".join(l.rstrip() for l in g)
    with open('spd.txt', encoding='utf-8', errors='ignore') as g:
        dateiSPD = " ".join(l.rstrip() for l in g)
    with open('linke.txt', encoding='utf-8', errors='ignore') as g:
        dateiLinke = " ".join(l.rstrip() for l in g)
    with open('cdu.txt', encoding='utf-8', errors='ignore') as g:
        dateiCDU = " ".join(l.rstrip() for l in g)
    with open('fdp.txt', encoding='utf-8', errors='ignore') as g:
        dateiFDP = " ".join(l.rstrip() for l in g)
    with open('AfD.txt', encoding='utf-8', errors='ignore') as g:
        dateiAfD = " ".join(l.rstrip() for l in g)

    # für schnelleres Auslesen können bestimmte Aktivitäten während der Tokenisierung noch ausgeschalten werden
    # (siehe Ausgabe Zeile 8)
    textGruene = nlp(dateiGruene)
    textSPD = nlp(dateiSPD)
    textLinke = nlp(dateiLinke)
    textCDU = nlp(dateiCDU)
    textFDP = nlp(dateiFDP)
    textAfD = nlp(dateiAfD)
    '''
    wordsGruene = [token.lemma_.lower() for token in textGruene if not token.is_stop and not token.is_punct and not token.is_space]
    wordsSPD = [token.lemma_.lower() for token in textSPD if not token.is_stop and not token.is_punct and not token.is_space]
    wordsLinke = [token.lemma_.lower() for token in textLinke if not token.is_stop and not token.is_punct and not token.is_space]
    wordsCDU = [token.lemma_.lower() for token in textCDU if not token.is_stop and not token.is_punct and not token.is_space]
    wordsFDP = [token.lemma_.lower() for token in textFDP if not token.is_stop and not token.is_punct and not token.is_space]
    wordsAfD = [token.lemma_.lower() for token in textAfD if not token.is_stop and not token.is_punct and not token.is_space]
    '''

    '''#sentsGruene = textGruene.sents
    #for sent in sentsGruene:
    #    print(list(sentsGruene))
    
    nouns = [token.lemma_ for token in textGruene if  not token.is_stop and
                                                            not token.is_punct and
                                                            not token.is_space and
                                                            (token.pos_ == 'NOUN' or
                                                             token.pos_ == 'PROPN')]
    
    verbs = [token.lemma_ for token in textGruene if  not token.is_stop and
                                                            not token.is_punct and
                                                            not token.is_space and
                                                            token.pos_ == 'VERB']
    '''
    wordsGruene = [token.lemma_ for token in textGruene if not token.is_stop and
                   not token.is_punct and
                   not token.is_space and
                   token.pos_ != 'NUM' and
                   not token.is_upper]
    wordsSPD = [token.lemma_ for token in textSPD if not token.is_stop and
                not token.is_punct and
                not token.is_space and
                token.pos_ != 'NUM' and
                not token.is_upper]
    wordsLinke = [token.lemma_ for token in textLinke if not token.is_stop and
                  not token.is_punct and
                  not token.is_space and
                  token.pos_ != 'NUM' and
                  not token.is_upper]
    wordsCDU = [token.lemma_ for token in textCDU if not token.is_stop and
                not token.is_punct and
                not token.is_space and
                token.pos_ != 'NUM' and
                not token.is_upper]
    wordsFDP = [token.lemma_ for token in textFDP if not token.is_stop and
                not token.is_punct and
                not token.is_space and
                token.pos_ != 'NUM' and
                not token.is_upper]
    wordsAfD = [token.lemma_ for token in textAfD if not token.is_stop and
                not token.is_punct and
                not token.is_space and
                token.pos_ != 'NUM' and
                not token.is_upper and
                not token.text == 'AfD']

    '''noun_freq = Counter(nouns)
    most_freq_nouns = noun_freq.most_common(10)
    
    
    for noun in most_freq_nouns:
        print(noun)
    
    
    print('\n')
    verb_freq = Counter(verbs)
    most_freq_nouns = verb_freq.most_common(10)
    for verb in most_freq_nouns:
        print(verb)
    '''

    word_freq = Counter(wordsGruene)
    word_freq1 = Counter(wordsSPD)
    word_freq2 = Counter(wordsLinke)
    word_freq3 = Counter(wordsCDU)
    word_freq4 = Counter(wordsFDP)
    word_freq5 = Counter(wordsAfD)

    w1 = most_freq_nouns = word_freq.most_common(50)
    most_freq_nouns1 = word_freq1.most_common(50)
    most_freq_nouns2 = word_freq2.most_common(50)
    most_freq_nouns3 = word_freq3.most_common(50)
    most_freq_nouns4 = word_freq4.most_common(50)
    most_freq_nouns5 = word_freq5.most_common(50)

    listG = []
    i = 0
    for word in most_freq_nouns:
        listG.insert(i, word)
        i += 1
        print(word)
    print('\n')
    print(listG)
    print('\n')

    listX = []
    listY = []
    i = 0
    for (x, y) in listG:
        listX.insert(i, x)
        listY.insert(i, y)
        i += 1
    print(listX)
    print('\n')
    print(listY)
    print('\n')

    # print(word_freq)
    print('\n')

    x = np.arange(50)
    plt.xticks(x, listX)
    plt.bar(listX, listY, color='blue')
    plt.savefig('graphGruene.png')
    plt.show()

    for word in most_freq_nouns1:
        print(word)
    print('\n')

    for word in most_freq_nouns2:
        print(word)
    print('\n')

    for word in most_freq_nouns3:
        print(word)
    print('\n')

    for word in most_freq_nouns4:
        print(word)
    print('\n')

    for word in most_freq_nouns5:
        print(word)

    '''
    # linesGruene = textGruene.split('\n')
    # linesSPD = textSPD.split('\n')
    
    # print([ line.split(" ") for line in textGruene])
    
    # doc = [line.split(" ") for line in textSPD]
    
    # print([token for token in textGruene])
    
    # docSPD = list(nlp.pipe((linesSPD)))
    # docGruene = list(nlp.pipe(linesGruene))
    
    
    # print(token for token in docGruene)
    
    import pandas as pd
    dataFrameGruene = pd.DataFrame({'Token': [token.text for token in textGruene],
                  'Lemma': [token.lemma for token in textGruene],
                  'POS': [token.pos_ for token in textGruene],
                  'Tag': [token.tag_ for token in textGruene],
                  'Dep': [token.dep_ for token in textGruene]})
    
    #print(dataFrameGruene.filter(dataFrameGruene.Tag.__getattr('_SP')))
    indexFilter1 = dataFrameGruene[dataFrameGruene['Tag'] == '_SP'].index
    indexFilter2 = dataFrameGruene[dataFrameGruene['POS'] == 'NUM'].index
    indexFilter3 = dataFrameGruene[dataFrameGruene['POS'] == 'PUNCT'].index
    indexFilter4 = dataFrameGruene[dataFrameGruene['POS'] == 'X'].index
    indexFilter5 = dataFrameGruene[dataFrameGruene['Tag'] == 'ART'].index
    indexFilter6 = dataFrameGruene[dataFrameGruene['Tag'] == 'KON'].index
    #indexFilter6 = dataFrameGruene[dataFrameGruene['POS'] == 'PROPN'].index
    
    dataFrameGruene.drop(indexFilter1, inplace=True)
    dataFrameGruene.drop(indexFilter2, inplace=True)
    dataFrameGruene.drop(indexFilter3, inplace=True)
    dataFrameGruene.drop(indexFilter4, inplace=True)
    dataFrameGruene.drop(indexFilter5, inplace=True)
    dataFrameGruene.drop(indexFilter6, inplace=True)
    #print(dataFrameGruene)
    
    indexFilter7 = dataFrameGruene[dataFrameGruene['Tag'] != 'NN'].index
    df = dataFrameGruene
    dataFrameGruene.drop(indexFilter7, inplace=True)
    #print(dataFrameGruene)
    
    indexFilter8 = dataFrameGruene[dataFrameGruene['POS'] != 'ADJ'].index
    df.drop(indexFilter8, inplace=True)
    #print(dataFrameGruene)
    
    derived_dataFrameGruene = dataFrameGruene[['Token']]
    #print(derived_dataFrameGruene)
    
    #data = [(docGruene, {'id': 1}), (docGruene, {'id': 2})]
    
    #print(data.__len__())
    #print(data[0])
    #print('\n')
    #print(data[1])
    
    
    # dateiGruene = nlp(dateiGruene.txt, encoding='utf-8, )
    # print(dateiGruene.txt)
    # dateiGruene.close()
    '''
