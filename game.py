from random import randint 

win_options = {1: [[2,3], [5,9], [4,7]], 2: [[1,3], [5,8]], 3: [[1,2], [5,7], [6,9]], 4: [[1,7], [5,6]], 5: [[2,8], [4,6], [1,9], [3,7]], 6: [[3,9], [4,5]],\
           7: [[1,4], [8,9], [3,5]], 8: [[2,5], [7,9]], 9: [[3,6], [1,5], [7,8]]}

def win_check(win_options, chosenplayer, choice, player):
    for i in win_options[choice]:
        if set(i).issubset(chosenplayer):
            if player == 1:
                print("win")
            else:
                print("loss")
            return True
    return False

def bot_move(chosenbot, avaliable):
    randomchoice = randint(1,len(avaliable))
    chosenbot.append(avaliable[randomchoice-1])
    avaliable.remove(avaliable[randomchoice-1])
    return randomchoice




avaliable = [1,2,3,4,5,6,7,8,9]

chosenbot = []
chosenplayer = []
end = False

while len(avaliable) > 0 and not end:
    print("please pick a location")
    for i in avaliable:
        print(i)
    while True:
        choice = int(input()) 
        if choice not in avaliable:
            print("select a avaliable square")
        else:
            break
    avaliable.remove(choice)
    chosenplayer.append(choice)

    if win_check(win_options, chosenplayer, choice, 1):
        break

    end = end | win_check(win_options, chosenbot, bot_move(chosenbot, avaliable), 0)
    print(chosenplayer)
    print(chosenbot)
    print(avaliable)