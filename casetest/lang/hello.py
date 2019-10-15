print('Hello World!')
print('What is your name?')
myName=input()
print('It is good to meet you, '+myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge=input()
print('You will be '+str(int(myAge)+1)+' in a year.')

if myName=='Alice':
    print('Hi, Alice')
elif myAge<12:
    print('You are not Alice, kiddo.')
elif myAge>2000:
    print('Unlike you, Alice is not an undead, imortal vampire.')
elif myAge>100:
    print('You are not Alice, grannie.')
    
# This is a python comment
