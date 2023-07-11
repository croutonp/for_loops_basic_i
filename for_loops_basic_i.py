BASIC
i = 0

while i <= 150:
    print(i)
    i += 1

MULTIPLES OF FIVE
i = 5

for i in range(5,1005,5):
    print(i)

COUNTING
i = 1

while i <=100:
    if i % 10 == 0 :
        print ("coding dojo")
    elif i % 5 == 0:
        print("coding")
    else:
        print(i)
    i += 1
HUGE
i = 0
sum = 0

while i <= 500000:
    if i % 2 != 0:
        sum = sum + i
        i = i + 1 
    else:
       i += 1

print(sum)


COUNTDOWN

i = 2022

while i >= 0:
    
    i -= 4
    if i > 0:
        print(i) 

FLEXIBLE

def flexibleCounter(lowNum,highNum,mult):

    while lowNum <= highNum:
        if lowNum % mult == 0:
            print(lowNum)
            lowNum += 1
        else:
            lowNum +=1

flexibleCounter(2,20,3)
