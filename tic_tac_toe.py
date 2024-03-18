
def sum(a, b, c):
    return a + b + c


def printBoard(xState, yState):
    zero = 'x' if xState[0] else ('o' if yState[0] else 0)
    one = 'x' if xState[1] else ('o' if yState[1] else 1)
    two = 'x' if xState[2] else ('o' if yState[2] else 2)
    three = 'x' if xState[3] else ('o' if yState[3] else 3)
    four = 'x' if xState[4] else ('o' if yState[4] else 4)
    five = 'x' if xState[5] else ('o' if yState[5] else 5)
    six = 'x' if xState[6] else ('o' if yState[6] else 6)
    seven = 'x' if xState[7] else ('o' if yState[7] else 7)
    eight = 'x' if xState[8] else ('o' if yState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")


def checkWin(xState, yState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("'x' won the match")
            return 1
        if(sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3):
            print("'o' won the match")
            return 0
        return -1


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("welcome to tic tac toe developed by --prince__kumar__gupta--")
    while True:
        printBoard(xState, yState)
        if (turn == 1):
            print("'x' chance to choose the position on the board")
            value = int(input("enter the position on the board from '0-8' : "))
            xState[value] = 1
        else:
            print("'y' chance to choose the position on the board")
            value = int(input("enter the position on the board from '0-8' : "))
            yState[value] = 1
        cwin = checkWin(xState, yState)
        if (cwin != -1):
            print("match over")
            break

        turn = 1-turn


