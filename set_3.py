def relationship_status(from_member, to_member, social_graph):

    from_follows_to = to_member in social_graph.get(from_member, {}).get("following", [])
    to_follows_from = from_member in social_graph.get(to_member, {}).get("following", [])

    if from_follows_to and to_follows_from: 
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by" 
    else:
        return "no relationship" 
    

def tic_tac_toe(board):
   
    dimension=len(board)
    
    for row in board: 
        if len(set(row))==1 and row[0]!="":
            return row[0]

    for slot_column in range(dimension): 
        column = [board[row][slot_column] for row in range(dimension)]
        if len(set(column))==1 and column[0]!="": 
            return column[0]

    left_right_diagonal = [board[i][i] for i in range(dimension)]
    right_left_diagonal = [board[i][dimension-i-1] for i in range(dimension)]
    
    if len(set(left_right_diagonal))==1 and left_right_diagonal[0]!="": 
        return left_right_diagonal[0]
    
    if len(set(right_left_diagonal))==1 and right_left_diagonal[0]!="": 
        return right_left_diagonal[0]        
    
    return "NO WINNER" 


def eta(first_stop, second_stop, route_map):

    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop: 
        for (start, finish), details in route_map.items():
            if start == current_stop: 
                total_time += details['travel_time_mins']
                current_stop = finish 
                break
            
    return total_time 