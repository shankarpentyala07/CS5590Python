#Check if all alphabets are present
def checkletters():
 for alphabet in alphabets:
    if alphabet not in strupper:
        return 'The input string does not contains all alphabets'
 return 'The input string contains all alphabets'
#Take input
str= input('Please enter a string of your choice')
#convert to upper case
strupper=str.upper()
alphabets ="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
#call the function checkletters
print(checkletters())



