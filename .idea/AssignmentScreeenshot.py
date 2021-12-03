import random



list = [[],[],[],[],[]]
for i in range(5):

    for j in range (6):
        a = random.randint(1,59)
        list[i].append(a)
        print(list[i])
win = random.choice(list)
print('the winner is',win)