#Taking number as input
number=int(input('Please enter a number\n'))
#Declare dictionary
dict={}
#Initalize dictionary key and values
for n in range(number):
    temp=n+1
    dict[temp] = temp*temp
#Print dictionary
print('Output dictionary is')
print(dict)