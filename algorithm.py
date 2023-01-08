board = []
playerX = []
playerO = []
value = ""


def check_win(O, X):
    global turn
    win = False
    result = ""
    win_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for comb in win_combos:
        if win !=True: color_w = []
        for num in comb:
            if turn % 2 == 1 and win == False:
                if num in O:
                    color_w.append(num)
                    if len(color_w) == 3:
                        win = True
                        result = "'O'"
                        break
                else: break
            elif win == False:
                if num in X:
                    color_w.append(num)
                    if len(color_w) == 3: 
                        win = True
                        result = "'X'"
                else: break
    if result == "" and turn == 10: result = "-"
    return scores[result]

def minimax(board, depth, isMaximazing):
    global playerO, playerX, value, turn
    result = check_win( playerO, playerX)
    if result != -10:
        return result
    if isMaximazing == True:
        bestScore = -10
        score = -10
        i = 0
        for i in range(1,10):
            if i in board:
                continue
            else:
                if value == "yes": 
                    playerX.append(i)
                else: playerO.append(i)
                turn += 1
                board = playerX + playerO
                score = minimax(board, depth+1, False)
                if value == "yes": 
                    playerX.remove(i)
                else: playerO.remove(i)
                board = playerX + playerO
                turn = turn - 1
                bestScore = max(bestScore,score)
        return bestScore
    else:
        bestScore = 10
        score = 10
        i = 0
        for i in range(1,10):
            if i in board:
                continue
            else:
                if value == "yes": 
                    playerO.append(i)
                else: playerX.append(i)
                turn += 1
                board = playerX + playerO
                score = minimax(board, depth+1, True)
                if value == "yes": 
                    playerO.remove(i)
                else: playerX.remove(i)
                turn = turn - 1
                board = playerX + playerO
                bestScore = min(score,bestScore)
        return bestScore

def best_move(O, X, val, t):
    global playerX, playerO, board, value, scores, turn
    value = val
    turn = t
    if turn ==1: return 1
    if value == "yes":
        scores = {"-": 0, "'X'": 1, "'O'": -1, "": -10}
    else: scores = {"-": 0, "'X'": -1, "'O'": 1, "":-10}
    playerO = O
    playerX = X
    board = playerO + playerX
    bestScore = -10
    bestMove = 0
    i = 0
    while i < 10:
        i += 1
        if i in board:
            continue
        else:
            if value == "yes": 
                playerX.append(i)
            else: playerO.append(i)
            turn += 1
            board = playerX + playerO
            score = minimax(board, 0, False)
            if score == None: score = -1
            if value == "yes": 
                playerX.remove(i)
            else:  playerO.remove(i)
            turn = turn - 1
            board = playerX + playerO
            if score > bestScore:
                bestScore = score
                bestMove = i
    return bestMove
