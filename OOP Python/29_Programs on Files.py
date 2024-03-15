# Q.1=> Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'
# f=open('OOP Python/q1_poems.txt')
# t=f.read()
# if 'twinkle' in t.lower():
#     print('Twinkle is Present')
# else:
#     print('Twinkle is not Present')

# Q.2=> The Game() function in a program lets a user play a game and returns the score as an integer.You need to read a file 'HiScore.txt' which is either blank or contains the previous Hi-Score. You need to write a program to update the Hi-Score whenever Game() breaks the Hi-Score.
# def Game():
#     return 1000
# score=Game()
# with open('OOP Python/q2_HiScore.txt') as f:
#     hiScoreStr=f.read()
# if hiScoreStr=='' or int(hiScoreStr)<score:
#     with open('OOP Python/q2_HiScore.txt','w') as f:
#         f.write(str(score))

# Q.3=> WAP to generate multiplication tables from 2 to 20 and write it to the different files.Place these files in a folder.
# for i in range(2, 21):
#     with open(f"OOP Python/tables/Multiplication_Table_of_{i}.txt",'w') as f:
#         for j in range(1,11):
#             f.write(f'{i} X {j} = {i*j}')
#             if j!=10:
#                 f.write('\n')

# Q.4=> A file contains list of words.You need to write a program which replaces these words with !@#$%& by updating the same file.
# words=['Monkey','Chimkandi','motee']
# with open('OOP Python/q4_words.txt') as f:
#     content=f.read()
# for i in words:
#     content=content.replace(i,'!@#$%&')
#     with open('OOP Python/q4_words.txt','w') as f:
#         f.write(content)

# Q.5=> WAP to find out the line number where 'python' is present.
# content =''
# i= 1
# with open('OOP Python/q5_log.txt') as f:
#     while True:
#         content=f.readline()
#         if 'python' in content.lower():
#             print(content)
#             print(f'Yes Python is present on line number {i}')
#         i+=1

# Q.6=> WAP to make a copy of a text file 'this.txt'
# with open('OOP Python/q6_this.txt') as f:
#     content=f.read()
# with open('OOP Python/q6_copy.txt','w') as f:
#     f.write(content)

# Q.7=> WAP to find out whether a file is identical & matches the content of another file.
# file1='OOP Python/q6_this.txt'
# file2='OOP Python/q6_copy.txt'
# with open(file1) as f:
#     f1=f.read()
# with open(file2) as f:
#     f2=f.read()
# if f1==f2:
#     print('Files are identical.')
# else:
#     print('Files are not identical')

# Q.8=> WAP to wipe out the contents of a file.
# filename='OOP Python/q8_wipeout.txt'
# with open(filename,'w') as f:
#     f.write('')