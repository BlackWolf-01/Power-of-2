#Program to check if a nummber is a power of 2
def power2(number):
    #As the power of 2 will have only one set bit, the n-1&n will always be 0
    if(number==0):
        return 0
    if((number&(~(number-1)))==number):
        return 1
    return 0
number=int(input('Enter the number'))
if (power2(number)):
    print('The number is a power of 2')
else:
    print('The number is not a power of 2')