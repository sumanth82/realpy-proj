# Enumerate takes an iterator ( E.g: a str - 'Hellooo' or a list [1,2,3] or a tuple (1,2,3)) and gives an index counter in the item that index

for i, char in enumerate('Hellooo'):
    print(i, char)

# O/P:

#0 H
#1 e
#2 l
#3 l
#4 o
#5 o
#6 o

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i, char)




