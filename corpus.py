## Paula Beatriz Louback Jardim

#!python -m spacy download en_core_web_sm

from bs4 import BeautifulSoup
from requests import get
import spacy
from string import punctuation

artigos = ["https://aliz.ai/en/blog/natural-language-processing-a-short-introduction-to-get-you-started/",
           "https://medium.com/nlplanet/two-minutes-nlp-python-regular-expressions-cheatsheet-d880e95bb468",
           "https://hbr.org/2022/04/the-power-of-natural-language-processing",
           "https://www.activestate.com/blog/how-to-do-text-summarization-with-python/",
           "https://towardsdatascience.com/multilingual-nlp-get-started-with-the-paws-x-dataset-in-5-minutes-or-less-45a70921d709"]

#matriz para guardar o vocabulario de cada documento
matriz = [[], [], [], [], []]

matriz_sentencas = []

i = 0
for site in artigos:
  sents_list = []
  document_words = set()

  r = get(site)
  r = r.content

  soup = BeautifulSoup(r, 'html.parser')
  text = soup.find_all('p')
  nlp = spacy.load("en_core_web_sm")

  for paragraph in text:
    content = paragraph.get_text()
    sentences = nlp(content).sents

    for sent in sentences:
      sents_list.append(sent)
      words = sent.text.split(" ")
      
      for word in words:
        word = word.strip(punctuation)
        document_words.add(word)

  matriz_sentencas.append(sents_list)
  for w in document_words:
    matriz[i].append(w)

  i += 1

count = 1
for doc in matriz_sentencas:
  print(f"Site {count}")
  print(f"Quantidade de sentenças: {len(doc)}")
  print(doc)
  count += 1