import re

import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# preprocessing
import nltk
from nltk.corpus import stopwords
from spacy.lang.de.stop_words import STOP_WORDS

nltk.download('stopwords')
import spacy

from datetime import datetime
import matplotlib.pyplot as plt

from enum import Enum


class Party(Enum):
    AFD = 0
    CDU = 1
    FDP = 2
    GRUENE = 3
    LINKE = 4
    SPD = 5


def prepare_data(parties: [Party]):
    # get sections
    sections = []
    for partie in parties:
        sections_of_partie = re.split(r'\n\s*\n', party_text[Party.FDP])
        sections.extend(sections_of_partie)

    partie_wordbags_mod = []

    for section in sections:
        partie_wordbag = gensim.utils.simple_preprocess(section)

        # filter stopwords
        partie_wordbag_spacy = [word for word in partie_wordbag if word not in all_stopwords]

        partie_wordbags_mod.append(partie_wordbag_spacy)

    # make bigrams
    bigram = gensim.models.Phrases(partie_wordbags_mod, min_count=5, threshold=100)
    # make trigrams
    trigram = gensim.models.Phrases(bigram[partie_wordbags_mod], threshold=100)

    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    def make_bigrams(texts):
        return [bigram_mod[doc] for doc in texts]

    def make_trigrams(texts):
        return [trigram_mod[bigram_mod[doc]] for doc in texts]

    def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        texts_out = []
        for sent in texts:
            doc = nlp(" ".join(sent))
            texts_out.append(
                [token.lemma_ for token in doc if token.pos_ in allowed_postags and token.lemma_ not in all_stopwords])
        return texts_out

    words_trigrams = make_trigrams(partie_wordbags_mod)
    words_lematized = lemmatization(words_trigrams)

    id2word = corpora.Dictionary(words_lematized)
    texts = words_lematized
    corpus = [id2word.doc2bow(text) for text in texts]

    return corpus, id2word, words_lematized


def plot_coherence_lda(coherence, max_topics, max_iterations, parties, iteration_intervall=25):
    corpus, id2word, words_lematized = prepare_data(parties)

    data = {}
    for iterations in range(iteration_intervall, max_iterations, iteration_intervall):
        statistics = {}
        for topics in range(1, max_topics):
            lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                        id2word=id2word,
                                                        num_topics=topics,
                                                        iterations=iterations
                                                        )
            coherence_model_lda = CoherenceModel(model=lda_model, texts=words_lematized, dictionary=id2word,
                                                 coherence=coherence, corpus=corpus)
            coherence_lda = coherence_model_lda.get_coherence()
            statistics[topics] = coherence_lda
        data[iterations] = statistics

    for key, value in data.items():
        plt.plot(list(value.keys()), list(value.values()), label=key)
    plt.legend()
    plt.xlabel('Number of topics')
    plt.ylabel('Coherence score')
    plt.title('Coherence score for different number of topics')

    plt.savefig(
        f'./graphs/coherence_score/lda/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_coherence_score_{coherence}_for_{parties[0]}_{len(parties)}.png')
    plt.show()

def plot_coherence_lsi(coherence, max_topics, parties):
    corpus, id2word, words_lematized = prepare_data(parties)

    statistics = {}
    for topics in range(1, max_topics):
        lda_model = gensim.models.lsimodel.LsiModel(corpus=corpus,
                                                    id2word=id2word,
                                                    num_topics=topics,
                                                    )
        coherence_model_lsi = CoherenceModel(model=lda_model, texts=words_lematized, dictionary=id2word,
                                             coherence=coherence, corpus=corpus)
        coherence_lsi = coherence_model_lsi.get_coherence()
        statistics[topics] = coherence_lsi

    plt.plot(list(statistics.keys()), list(statistics.values()))
    plt.legend()
    plt.xlabel('Number of topics')
    plt.ylabel('Coherence score')
    plt.title('Coherence score for different number of topics')

    plt.savefig(
        f'./graphs/coherence_score/lsi/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_coherence_score_{coherence}_for_{parties[0]}_{len(parties)}.png')
    plt.show()

if __name__ == '__main__':
    # preprocessing
    nlp = spacy.load('de_core_news_md')

    # stopwords
    nltk_stopwords = stopwords.words('german')

    # build stopwords list
    all_stopwords = list(set(STOP_WORDS) | set(nltk_stopwords))
    with open('custom_stopwords.txt', 'r', encoding='utf-8') as f:
        all_stopwords += [line.strip() for line in f.readlines()]

    # Load files
    party_text = {}
    for party in Party:
        all_stopwords.extend(['{}'.format(party.name.lower())])
        with open('resources/' + party.name + '.txt', encoding='utf-8', errors='ignore') as txt:
            file = " ".join(l for l in txt)
            # remove gender *
            file = re.sub(r'\*innen(\w*)\s', r'\1 ', file)
        party_text[party] = file

    all_parties = [p for p in Party]



    plot_coherence_lda('u_mass', max_iterations=225, max_topics=20, parties=all_parties)
