from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
import operator
#input the file
file1=open('input.txt','r')
#reading the file
line =file1.readline()
lemma=WordNetLemmatizer()
dict={}
print('processing Lemmatization and removal of verbs')
while line !="":
    words=word_tokenize(line)
    for x in words:
        lemma1=lemma.lemmatize(x)
        pos =pos_tag([lemma1])
        postype=pos[0][1][0:1]
        if not str(postype).__eq__('V') and \
                not lemma1.__eq__('.') and not lemma1.__eq__(','):
         if lemma1 in dict:
                dict[lemma1] = dict[lemma1]+1
         else:
                dict[lemma1]=1
    line=file1.readline()
print('word frequency')
for key,value in dict.items():
    print(key,':',value)
sorted_dict=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
print('Top 5 words that has been repeated most')
top5words=[]
summary=""
for x in sorted_dict[:5]:
    print(x[0])
    top5words.append(x[0])
print('Generating summary')
with open('input.txt') as fin:
   line= fin.readline()
   while line !="":
       sentences=sent_tokenize(line)
       for sentence in sentences:
        for topword in top5words:
           if topword in sentence:
               summary += sentence
               break
       line=fin.readline()
print('summary of input file:',summary)







