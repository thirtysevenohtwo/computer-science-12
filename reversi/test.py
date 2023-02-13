board = [[" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", "●", "○", " ", " ", " "],
         [" ", " ", " ", "●", "●", " ", " ", " "],
         [" ", " ", " ", "●", "○", "●", " ", " "],
         [" ", " ", " ", " ", "○", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "]]

def evaluate(board):
    black = 0
    white = 0
    for y in board:
        for x in y:
            if x != " " and x == "●":
                white += 1
            elif x != " " and x == "○":
                black += 1
    if black == white:
        return 0
    elif black > white:
        return black
    else:
        return white
    
print(evaluate(board))