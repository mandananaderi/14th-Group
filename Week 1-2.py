
print('Hopwiz-Game', '****************************************************')

print('solution 1 :')

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "hopviz")
    elif 0 == i % 3:
        print(i, "hop")
    elif i % 5 == 0:
        print(i, "viz")
    else:
        print(i)

print('solution 2 :')

myGame = []
for i in range(101):
    myGame.append('hopwiz' if i in range(0, 101, 15) else 'hop' if i in range(0, 101, 3) else 'wiz' if i in range(0, 101, 5) else int(i))

print(myGame)

print('Prime-Numbers in (1 - 1000)', '****************************************************')

print('solution 1 :')

for i in range(1, 1001):
     if i not in [1, 2, 3, 5] and (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
         continue
     else:
        print(i)

print('solution 2 :')

primeList = []
for i in range(1, 1001):
     if i not in (1, 2, 3, 5) and (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
         continue
     else:
         primeList.append(i)

print(primeList)

print('for loop to iterate backwards', '****************************************************')

print('solution 1 :')

myString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(myString[::-1])

print('solution 2 :')

if myString:
  print(myString[::-1])