def applyMove(board, move):
    for line in board:
        for nr in line:
            if nr[0] == int(move):
                nr[1] = True

def checkForWins(boards, nrMoves = 0):
    for i in range(0, len(boards)):
        for j in range(0,5):
            if boards[i][j][0][1] and boards[i][j][1][1] and boards[i][j][2][1] and boards[i][j][3][1] and boards[i][j][4][1]:
                return i
            elif boards[i][0][j][1] and boards[i][1][j][1] and boards[i][2][j][1] and boards[i][3][j][1] and boards[i][4][j][1]:
                return i
    return -1

def sumUnmarked(board):
    sum = 0
    for line in board:
        for nr in line:
            if not nr[1]:
                sum += nr[0]
    return sum

def play(moves, boards, nrMoves=0):
    for board in boards:
        applyMove(board, moves[0])
    won = checkForWins(boards, nrMoves)
    if won > -1:
        return (won, int(moves[0]))
    else:
        del moves[0]
        return play(moves, boards, nrMoves+1)

if __name__ == '__main__':
    with open("day4\\input.txt") as f:
        bingo = []
        for line in f:
            bingo.append(line)
        #print(bingo[0]) sanity check

        moves = bingo[0].split(",")
        #print(moves) sanity check
        boards = []
        for i in range(1, len(bingo), 6):
            board = []
            for j in range(1,6):
                stringLine = bingo[i+j].split()
                line = []
                if len(stringLine) > 0:
                    for k in range(0,5):
                        line.append([int(stringLine[k]), False])
                board.append(line)
            boards.append(board)

        winBoard = play(moves, boards)
        print("PART1: " + str(sumUnmarked(boards[winBoard[0]] * winBoard[1])))