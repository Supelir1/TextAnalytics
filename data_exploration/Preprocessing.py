
import spacy
# use eventually 'de_core_news_lg'
nlp = spacy.load('de_core_news_md')
print(nlp.pipe_names)

# mit Methode pipe(<datei>) und Path optimierbar(siehe Zeile 180)
with open('../resources/GRUENE.txt', encoding='utf-8', errors='ignore') as g:
    dateiGruene = " ".join(l.rstrip() for l in g)
with open('../resources/SPD.txt', encoding='utf-8', errors='ignore') as g:
    dateiSPD = " ".join(l.rstrip() for l in g)
with open('../resources/LINKE.txt', encoding='utf-8', errors='ignore') as g:
    dateiLinke = " ".join(l.rstrip() for l in g)
with open('../resources/CDU.txt', encoding='utf-8', errors='ignore') as g:
    dateiCDU = " ".join(l.rstrip() for l in g)
with open('../resources/FDP.txt', encoding='utf-8', errors='ignore') as g:
    dateiFDP = " ".join(l.rstrip() for l in g)
with open('../resources/AFD.txt', encoding='utf-8', errors='ignore') as g:
    dateiAfD = " ".join(l.rstrip() for l in g)


textGruene = nlp(dateiGruene)
textSPD = nlp(dateiSPD)
textLinke = nlp(dateiLinke)
textCDU = nlp(dateiCDU)
textFDP = nlp(dateiFDP)
textAfD = nlp(dateiAfD)

wordsGruene = [token.lemma_ for token in textGruene if not token.is_stop and
               not token.is_punct and
               not token.is_space and
               token.pos_ != 'NUM' and
               not token.is_upper]
wordsSPD = [token.lemma_ for token in textSPD if not token.is_stop and
            not token.is_punct and
            not token.is_space and
            token.pos_ != 'NUM' and
            not token.is_upper
            and token.text != '>']
wordsLinke = [token.lemma_ for token in textLinke if not token.is_stop and
              not token.is_punct and
              not token.is_space and
              token.pos_ != 'NUM' and
              not token.is_upper and
              token.text != '\uf0a7']
wordsCDU = [token.lemma_ for token in textCDU if not token.is_stop and
            not token.is_punct and
            not token.is_space and
            token.pos_ != 'NUM' and
            not token.is_upper]
wordsFDP = [token.lemma_ for token in textFDP if not token.is_stop and
            not token.is_punct and
            not token.is_space and
            token.pos_ != 'NUM' and
            token.text == 'Freie' and
            token.text == ' Demokraten' and
            not token.is_upper]
wordsAfD = [token.lemma_ for token in textAfD if not token.is_stop and
            not token.is_punct and
            not token.is_space and
            token.pos_ != 'NUM' and
            not token.is_upper and
            not token.text == 'AfD']

'''
#sentsGruene = textGruene.sents
#for sent in sentsGruene:
#    print(list(sentsGruene))
'''



def filterNouns(text):
    nouns = [token.lemma_ for token in text if not token.is_stop and
                                            not token.is_stop and
                                            not token.is_punct and
                                            not token.is_space and
                                            (token.pos_ == 'NOUN' or
                                             token.pos_ == 'PROPN')]
    return nouns

def filterverbs(text):
    verbs = [token.lemma_ for token in text if not token.is_stop and
                                            not token.is_punct and
                                            not token.is_space and
                                            token.pos_ == 'VERB']
    return verbs

def filterAdj(text):
    adjs = [token.lemma_ for token in text if not token.is_stop and
                                            not token.is_punct and
                                            not token.is_space and
                                            token.pos_ == 'ADJ']
    return adjs

def filterArg(sents):
    argus = [token.lemma_ for sent, token in sents if not token.is_stop and
                                            not token.is_punct and
                                            not token.is_space and
                                            (filterAdj(sent) or filterAdj(sent) and
                                             filterNouns(sent))]
                                            # TODO: condition for filtering argument
    return argus