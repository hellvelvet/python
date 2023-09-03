go = [[1, 0, 2, 2, 0, 0, 0, 0, 0],[2, 0, 0, 0, 2, 0, 1, 0, 0]]



def who_won(game_board: list):
    white = 0
    black = 0
    zero = 0
    for row in game_board:
        for square in row:
            if square == 1:
                white += 1
            elif square == 2:
                black += 1
            else:
                zero += 1
    if white > black and white > zero:
        return 1
    elif black > white and black > zero:
        return 2
    elif black == white:
        return 0
    else:
        return 0
    

print(who_won(go))
