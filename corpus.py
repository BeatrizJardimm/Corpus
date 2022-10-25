# Paula Beatriz Louback Jardim

# ------------------------------------------------------
### Enunciado ###

# Sua tarefa será transformar um conjunto de 5 sites, sobre o tema de processamento de linguagem natural em um conjunto de cinco listas distintas de sentenças.
# Ou seja, você fará uma função que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta url.
# Duas condições são importantes:

# a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 1000 palavras.  
# b) O texto desta página deverá ser transformado em um array de senteças.  
 
# Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca Spacy.

# ------------------------------------------------------
# Realizando os imports:
#!python -m spacy download en_core_web_sm

from bs4 import BeautifulSoup
from requests import get
from spacy import load
import string

# ------------------------------------------------------
# Guardando as referências para todos os artigos em uma lista:
artigos = ["https://aliz.ai/en/blog/natural-language-processing-a-short-introduction-to-get-you-started/",
           "https://medium.com/nlplanet/two-minutes-nlp-python-regular-expressions-cheatsheet-d880e95bb468",
           "https://hbr.org/2022/04/the-power-of-natural-language-processing",
           "https://www.activestate.com/blog/how-to-do-text-summarization-with-python/",
           "https://towardsdatascience.com/multilingual-nlp-get-started-with-the-paws-x-dataset-in-5-minutes-or-less-45a70921d709"]

# ------------------------------------------------------
# Esse código percorre todos os documentos, criando uma lista com as sentenças de cada documento
# e ao final, une todas essas listas em uma matriz.
# Ao mesmo tempo, o código abaixo realiza a mesma atividade descrita acima para o vocabulário de cada documento,
# criando uma lista de palavras para cada um e juntando essas listas no final. 

matriz_palavras = [[], [], [], [], []]
matriz_sentencas = []

i = 0
for site in artigos:
  sents_list = []
  document_words = set()

  r = get(site)
  r = r.content

  soup = BeautifulSoup(r, 'html.parser')
  text = soup.find_all('p')
  nlp = load("en_core_web_sm")

  for paragraph in text:
    content = paragraph.get_text()
    sentences = nlp(content).sents

    for sent in sentences:
      sent = sent.text.strip(string.punctuation)
      sent = sent.strip(string.digits)
      sent = sent.strip('\n')
      sents_list.append(sent)
      words = sent.split(" ")
      
      for word in words:
        word = word.strip(string.punctuation)
        word = word.strip(string.digits)
        word = word.strip('\n')
        document_words.add(word)

  matriz_sentencas.append(sents_list)
  for w in document_words:
    matriz_palavras[i].append(w)

  i += 1

count = 1
for doc in matriz_sentencas:
  print(f"Site {count}")
  print(f"Quantidade de sentenças: {len(doc)}")
  print(doc)
  print('\n')
  count += 1
