import nltk
from nltk.corpus import wordnet
from itertools import chain
synonyms=set()
file1=open('input.txt','r')
line =file1.readline()
while  line !="":
  words = line.split(" ")
  for word in words:
      for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.add(l.name())
      if synonyms:
       print('Synonyms of word ',word,' : ',synonyms)
       synonyms.clear()
  line=file1.readline()


