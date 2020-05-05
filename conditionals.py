# if and else if 

if 'a' < 'b':
    print('Condition was true')

if ('1' < '2'):
    print('Maybe 1 is less than 2')

if (10>20):
    print('10 is NOT GREATER THAN 20')
else:
    print('10 is LESS THAN 20')

###########  ELIF #####################


if 'b' < 'a':
    print('Test a')
elif 'b' > 'a':
    print('Test b')  # O/P: Test b
else:
    print('Dead End')


####

x = input('What is your Name?: ')

print(x)

if len(x) > 6:
    print('Name length exceeded')
elif len(x) < 2:
    print('Name length is too short')
else:
    print('Wonderful Name')

############# PASS ##########


name = 'Google'

if name == 'Google':
    print('apple')
else:
    pass


