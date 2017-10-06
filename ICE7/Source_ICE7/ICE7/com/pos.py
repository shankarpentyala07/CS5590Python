from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
file1=open('input.txt','r')
line =file1.readline()
print('POS tagging : ')
while line !="":
    words=word_tokenize(line)
    for x in pos_tag(words):
        print(x)
    line=file1.readline()
