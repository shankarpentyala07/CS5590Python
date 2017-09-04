#Find numbers which are divisible by 5 and multiple of 2 in a given range
def findnumbers():
    for x in range(lower,upper+1):
        if x % 5 == 0:
            if not x&1:
                print(x,end=',')



lower = int(input('Please enter the range start value'))
upper = int(input('Please enter the range high value'))
findnumbers()

