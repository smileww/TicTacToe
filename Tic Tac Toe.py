import random

win_combos = [[1,2,3],
              [4,5,6],
              [7,8,9],
              [1,4,7],
              [2,5,8],
              [3,6,9],
              [1,5,9],
              [3,5,7]]

num = 0
idx = 0

player = []
computer = []
options = [1,2,3,4,5,6,7,8,9]
winner = False
attempts = 9
d = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}


        
while not winner and attempts >0:
    #player 
    num=int(input('choose a num between 1 and 9: '))
    while num in player or num in computer:
      num = int(input('choose a different number: '))
    else:
      d[num] = 'X'
      options.remove(num)
      player.append(num)
    attempts -= 1
     
    #computer
    if len(options)>0:
        idx = random.choice(options)
        d[idx] = 'O'
        options.remove(idx)
        computer.append(idx)
        attempts -= 1
    
    #winning conditions
    if (d[1]=='X' and d[2]=='X' and d[3]=='X')or(d[4]=='X' and d[5]=='X' and d[6]=='X')or(d[7]=='X' and d[8]=='X' and d[9]=='X')or(d[1]=='X' and d[4]=='X' and d[7]=='X')or(d[2]=='X' and d[5]=='X' and d[8]=='X')or(d[3]=='X' and d[6]=='X' and d[9]=='X')or(d[1]=='X' and d[5]=='X' and d[9]=='X')or(d[3]=='X' and d[5]=='X' and d[7]=='X'):
        print('You won!')
        winner = True
        
    elif (d[1]=='O' and d[2]=='O' and d[3]=='O')or(d[4]=='O' and d[5]=='O' and d[6]=='O')or(d[7]=='O' and d[8]=='O' and d[9]=='O')or(d[1]=='O' and d[4]=='O' and d[7]=='O')or(d[2]=='O' and d[5]=='O' and d[8]=='O')or(d[3]=='O' and d[6]=='O' and d[9]=='O')or(d[1]=='O' and d[5]=='O' and d[9]=='O')or(d[3]=='O' and d[5]=='O' and d[7]=='O'):
        print('You lost!')
        winner = True

    #print board
    print('Board:')  
    print('1:',d[1],'2:',d[2],'3:',d[3])
    print('4:',d[4],'5:',d[5],'6:',d[6])
    print('7:',d[7],'8:',d[8],'9:',d[9])

if attempts == 0 and winner == False:
    print('A tie!')
   