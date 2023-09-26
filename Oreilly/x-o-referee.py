def checkio(game_result):
    seq = game_result[0]+game_result[1]+game_result[2]
    for i in range(3):
        if seq[i*3] == seq[i*3+1] == seq[i*3+2] != '.': return seq[i*3] # check row
        if seq[i] == seq[i+3] == seq[i+6] != '.': return seq[i] # check column

    if seq[0] == seq[4] ==seq[8] != '.': return seq[0] # check left diagonal
    if seq[2] == seq[4] ==seq[6] != '.': return seq[2] # check right diagonal
    return "D"
