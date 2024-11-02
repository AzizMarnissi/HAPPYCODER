def player(prev_play, opponent_history=None):
    
    if opponent_history is None:
        opponent_history = []

    
    if prev_play:
        opponent_history.append(prev_play)

    
    if prev_play == "R":
        return "P"  
    elif prev_play == "P":
        return "S"  
    elif prev_play == "S":
        return "R"  
    else:
       
        return "R"
