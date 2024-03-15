import random as r

# 1.Snake-Water-Gun Game

# def gameWin(comp,you):

#     # If two values are equal,declares a Tie.
#     if comp==you:
#         return None

#     # check for all possibilities when computer choose 'Snake'. 
#     elif comp=='s':
#         if you=='w':
#             return False
#         elif you=='g':
#             return True

#     # check for all possibilities when computer choose 'Water'.
#     elif comp=='w':
#         if you=='g':
#             return False
#         elif you=='s':
#             return True

#     # check for all possibilities when computer choose 'Gun'.
#     elif comp=='g':
#         if you=='s':
#             return False
#         elif you=='w':
#             return True

# print('Computer Turn: Snake(s) Water(w) or Gun(g)?')
# randNo=r.randint(1,3)
# if randNo==1:
#     comp='s'
# elif randNo==2:
#     comp='w'
# elif randNo==3:
#     comp='g'

# you=input('Your Turn: Snake(s) Water(w) or Gun(g)=>')
# a=gameWin(comp,you)

# print(f'Computer Choose {comp}')
# print(f'You Choose {you}')

# if a== None:
#     print('The Game is Tie!')
# elif a== True:
#     print('You Win!')
# else:
#     print('You Lose!')


# -----------------------------------------------------


# 2.Rock-Paper-Sessior Game

# def gameWin(comp,you):

#     # if two values are equal,declares a Tie
#     if comp==you:
#         return None
    
#     # check for all possibilities when computer choose 'Rock'
#     elif comp=='r':
#         if you=='p':
#             return True
#         elif you=='s':
#             return False
    
#     # check for all possibilities when computer choose 'Paper'
#     elif comp=='p':
#         if you=='s':
#             return True
#         elif you=='r':
#             return False
    
#     # check for all possibilities when computer choose 'Sessior'
#     elif comp=='s':
#         if you=='r':
#             return True
#         elif you=='p':
#             return False

# print('Computer Turn: Rock(r) Paper(p) or Sessior(s)?')
# randNo=r.randint(1,3)
# if randNo==1:
#     comp='r'
# elif randNo==2:
#     comp='p'
# elif randNo==3:
#     comp='s'

# you= input('Your Turn: Rock(r) Paper(p) or Sessior(s)?')
# a=gameWin(comp,you)

# print(f'Computer Choose {comp}')
# print(f'You Choose {you}')

# if a== None:
#     print('The Game is Tie!')
# elif a== True:
#     print('You Win!')
# else:
#     print('You Lose!')