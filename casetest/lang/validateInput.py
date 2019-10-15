#! python
while True:
    print('Enter your age:')
    age=input()
    if age.isdecimal():
        break
    print('Please enter a number for your age!')
while True:
    print('Select a new password(letters and numbers only):')
    password=input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers!')
age=int(age) 
if age<25:
    print('Access granted young man.');
elif age>=50:
    print('Access granted grandpa.');
else:
    print('Access granted sir.');
