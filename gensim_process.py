from gensim.summarization import summarize
from gensim import corpora, models, similarities
import pandas as pd
import os



def get_text_abstract(filepath):
    names = os.listdir(filepath)
    texts = []
    abstracts = []
    for name in names:
        filename = filepath+name
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        abstract = summarize(text)
        texts.append(text)
        abstracts.append(abstract)
    return texts, abstracts, names


def GenDictandCorpus(documents):
    texts = [[word for word in document.lower().split()] for document in documents]

    
    dictionary = corpora.Dictionary(texts)
   
    corpus = [dictionary.doc2bow(text) for text in texts]
    print(dictionary)
    print(corpus)
    return dictionary, corpus


def Tfidf(text):
    dictionary, corpus = GenDictandCorpus(text)

    tfidf = models.TfidfModel(corpus)

    corpus_tfidf = tfidf[corpus]
    # print(len(corpus_tfidf))
    for doc in corpus_tfidf:
        print(doc)
    print(len(corpus_tfidf))

    return corpus_tfidf, dictionary


def save_to_file(filepath):
    documents, abstracts, names = get_text_abstract(filepath)
    corpus_tfidf, dictionary = Tfidf(documents)
    results = []
    assert len(documents) == len(corpus_tfidf)
    for i in range(len(names)):
        result = []
        result.append(names[i].split('.')[0])
        result.append(abstracts[i])
        tfidf = corpus_tfidf[i]
        # print(tfidf)
        tfidf.sort(key=lambda e:e[1], reverse=True)
        # print(tfidf)
        for j in range(3):  
   
            result.append((dictionary[tfidf[j][0]], tfidf[j][1]))
        results.append(result)
    print(results[0])
    print(len(results[0]))
    pd.DataFrame(results, columns=['filename', 'abstract', 'top1', 'top2', 'top3']).to_excel('data/results.xlsx', index=False)


if __name__ == '__main__':
    save_to_file('data/article/')





