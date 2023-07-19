from random import randint 

positions = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1, 9: -1}

win_options = {1: [[2,3], [5,9], [4,7]], 2: [[1,3], [5,8]], 3: [[1,2], [5,7], [6,9]], 4: [[1,7], [5,6]], 5: [[2,8], [4,6], [1,9], [3,7]], 6: [[3,9], [4,5]],\
           7: [[1,4], [8,9], [3,5]], 8: [[2,5], [7,9]], 9: [[3,6], [1,5], [7,8]]}


def options(places):
    playable = []
    for i in places:
        if places[i] == -1:
            playable.append(i)
    return playable 

def win_check(win_options, chosenplayer, choice, player):
    for i in win_options[choice]:
        if set(i).issubset(chosenplayer):
            if player == 1:
                print("win")
            else:
                print("loss")
            return True
    return False


chosenbot = []
chosenplayer = []
end = False

while -1 in positions.values() and not end:
    print("please pick a location")
    for i in options(positions):
        print(i)
    choice = int(input())
    chosenplayer.append(choice)
    positions[choice] = 1

    if win_check(win_options, chosenplayer, choice, 1):
        break


    while True:
        a
        if a not in chosenplayer:
            chosenbot.append(a)
            positions[a] = 0
        end = end | win_check(win_options, chosenplayer, choice, 0)
    print("hi")
