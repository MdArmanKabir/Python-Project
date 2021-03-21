bord = [' _ '] * 9
print(bord[0:8])


def print_bord():
    print(bord[0], '|', bord[1], '|', bord[2])
    print(bord[3], '|', bord[4], '|', bord[5])
    print(bord[6], '|', bord[7], '|', bord[8])


def is_valid_location(player):
    global bord
    global position
    if bord[position] == ' _ ':
        bord[position] = player

    else:
        print('invalid location! you lost your turn')


def wining_condition(player):
    global bord
    global game
    if (bord[0] == bord[1] == bord[2] == player != ' _ ') or (bord[3] == bord[4] == bord[5] == player != ' _ ') or (
            bord[6] == bord[7] == bord[8] == player != ' _ '):
        return True
    elif (bord[0] == bord[3] == bord[6] == player != ' _ ') or (bord[1] == bord[4] == bord[7] == player != ' _ ') or (
            bord[2] == bord[5] == bord[8] == player != ' _ '):
        return True
    elif (bord[0] == bord[4] == bord[8] == player != ' _ ') or (bord[2] == bord[4] == bord[6] == player != ' _ '):
        return True
    elif bord[0] != ' _ ' and bord[1] != ' _ ' and bord[2] != ' _ ' and bord[3] != ' _ ' and bord[4] != ' _ '\
            and bord[5] != ' _ ' and bord[6] != ' _ ' and bord[7] != ' _ ' and bord[8] != ' _ ':
        print('match tie..!')


print_bord()

game = True
turn = 0
# game loop
while game:

    if turn == 0:
        position = int(input('player 1 select: ')) - 1
        is_valid_location(' X ')
        print_bord()
        turn = 1
        if wining_condition(' X '):
            print('player 1 win..!')
            break

    else:
        position = int(input('player 2 select: ')) - 1
        is_valid_location(' O ')
        print_bord()
        turn = 0
        if wining_condition(' O '):
            print('player 2 win..!')
            break
