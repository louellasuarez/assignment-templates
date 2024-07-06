'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

if from_member in social_graph[to_member].get("following", []) and to_member in social_graph[from_member].get("following", []): 
        out = "friends"
    elif from_member in social_graph[to_member].get("following", []) and to_member not in social_graph[from_member].get("following", []):
        out = "followed by"
    elif from_member not in social_graph[to_member].get("following", []) and to_member in social_graph[from_member].get("following", []):
        out = "follower"
    else:
        out = "no relationship"
    return out 


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    for row in board: #horizontal
        if all(letter==row[0] and letter for letter in row): 
            out=row[0]
            
    for column in range(len(board)): #vertical
        if all(row[column]==board[0][column] and row[column] for row in board):
            out=board[0][column]
            
    if all(board[0][0]==board[i][i] and board[i][i] for i in range(len(board))): #diagonal\
        out=board[0][0]
    elif all(board[i][len(board) - i - 1] == board[0][len(board)-1] and board[0][len(board)-1] for i in range(len(board))): #diagonal/
        out=board[0][len(board)-1]
        
    return out

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    new_route_map = []
    for pair, value in route_map.items(): 
        new_route_map.append( ( pair[0], pair[1], value['travel_time_mins'] ) )
    first_leg = next(leg for leg in new_route_map if leg[0]==first_stop)
    next_stop = first_leg[1]
    time = first_leg[2]
    
    while next_stop!=second_stop:
        leg = next(leg for leg in new_route_map if leg[0]==next_stop)
        time += leg[2]
        next_stop = leg[1]
        
    return time
