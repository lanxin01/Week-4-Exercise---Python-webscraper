# Week-4-Exercise---Python-webscraper

Description

Keywords are a group of words that represent the important content of an article, and have important applications in document retrieval, automatic summarization, and text classification. In reality, a large number of texts do not contain keywords, which makes it more difficult to obtain text information conveniently. Therefore, the technology of automatically extracting keywords has important value and significance.

I use gensim's tfidf to get the keyword of each document, which means that the keyword is relative to this document and other documents. First, I want to calculate word frequency. In order to facilitate the comparison of different articles, the "word frequency" standardization is carried out. Then I use a corpus (corpus) to simulate the use environment of the language. If a word is more common, then the denominator is fine, and the inverse document frequency is smaller and closer to 0. TF-IDF and a word in the document. Therefore, the algorithm for automatically extracting keywords is very clear. It is to calculate the TF-IDF value of each word in the document, and then sort it in descending order, and then I use gensim's summary.summarize Go back to the summary of each document, that is, summarize each document.

Result:
![image](https://github.com/lanxin01/Coding-2-Lab-Work/blob/main/%E6%88%AA%E5%B1%8F2021-04-26%20%E4%B8%8B%E5%8D%883.28.49.png)
![image](https://github.com/lanxin01/Coding-2-Lab-Work/blob/main/%E6%88%AA%E5%B1%8F2021-04-26%20%E4%B8%8B%E5%8D%883.29.03.png)
