

from random import randint


print("test")


allocation = 0.
ctr=0

loop=0
winCount = 0
while loop < 1000:
    maxLoop = 100
    startval = 100
    ctr = 0
    while startval > 10 and maxLoop > ctr: 
        bet = startval * allocation
        cash = startval - bet
        win = 0
        #print('[' + str(ctr) + ']'+'start value: ' + str(startval) + ' bet: ' + str(bet), end=' ')
        if randint(0,1):
            #print('W', end=' ')
            startval = cash + bet * 2
        else:
            #print('L', end=' ')
            startval = cash + bet * 0.5
        #print(' Bal:' + str(startval))
        #print('')
        ctr = ctr+1
    loop = loop + 1
    #print('[' + str(loop) + ']'+'maxLoop: ' + str(maxLoop)+' startval: ' + str(startval))
    if startval > 200:
        winCount = winCount + 1

print('Summary Win Rate : '+ str(winCount/1000))