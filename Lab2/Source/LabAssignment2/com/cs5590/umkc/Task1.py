#Take input from the user
sentence = input('Please enter a sentence\n')
#Declare an empty set
myset=set()
#Adding words to set to eliminate duplicate words
for word in sentence.split(" "):
    myset.add(word)
#using the sorted function to sort set and it returns sorted set as list
myset =sorted(myset)
#list to string
sentence =' '.join(myset)
print(sentence)

