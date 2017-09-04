# calculate word frequency in a file
def process():
    print("Started processing the file")
    file = open('textfile1','r')
    line = file.readline()
    hashmap ={}
    while line !="":
#read line by line
        for word in line.split(" "):
            if not  word in hashmap:
               hashmap[word]=1
            else:
                hashmap[word] = hashmap[word]+1
        line=file.readline()

#Print the output
    for key,value in hashmap.items():
        print(key,':',value)
#call the function
process()

