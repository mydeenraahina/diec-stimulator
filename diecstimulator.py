import random
print("welcome to die stimulator game")
def roll():
    x=random.randint(1,5)
    print('dice rolling')
    print("the value is....",x)
while True:
    a=input('enter your choice:')
    if a=="y":
        roll()
    else:
        print('!')
        break;
