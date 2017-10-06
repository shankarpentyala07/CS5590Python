from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
file1=open('input.txt','r')
text =file1.readline()
print('NER is present in the parse tree : ')
while text !="":
    sent3=ne_chunk(pos_tag(word_tokenize(text)))
    print(sent3)
    text=file1.readline()