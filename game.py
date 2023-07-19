positions = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1, 9: -1}

options = {1: [[2,3], [5,9], [4,7]], 2: [[1,3], [5,8]], 3: [[1,2], [5,7], [6,9]], 4: [[1,7], [5,6]], 5: [[2,8], [4,6], [1,9], [3,7]], 6: [[3,9], [4,5]],\
           7: [[1,4], [8,9], [3,5]], 8: [[2,5], [7,9]], 9: [[3,6], [1,5], [7,8]]}

print(set(options[1][0]).issubset(set([2,3,5])))

chosenbot = []
chosenplayer = []
end = False
while -1 in positions.values() and not end:
    print("please pick a location")
    for i in positions:
        if positions[i] == -1:
            print(i)
    choice = int(input())
    chosenplayer.append(choice)
    positions[choice] = 1
    for i in options[choice]:
        if set(i).issubset(chosenplayer):
            print("win") 
            end = True
