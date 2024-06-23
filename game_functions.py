from tkinter import Canvas
from gui import draw_O, draw_X

def is_game_over(game_state : list[str]):

    winning_combinations = [
        (0, 1, 2),  # Row 1
        (3, 4, 5),  # Row 2
        (6, 7, 8),  # Row 3
        (0, 3, 6),  # Column 1
        (1, 4, 7),  # Column 2
        (2, 5, 8),  # Column 3
        (0, 4, 8),  # Diagonal 1
        (2, 4, 6)   # Diagonal 2
    ]

    for combo in winning_combinations:
        if game_state[combo[0]] == game_state[combo[1]] == game_state[combo[2]] and game_state[combo[0]] != ' ':
            return game_state[combo[0]]

    if ' ' not in game_state:
        return "Draw"
    
    return ""

# Calculate AI's best move and draw X on board
def ai_turn(game_state : list[str],
            symbol_map : dict,
            canvas : Canvas,
            tile_bindings : list[str]
            ):
    
    ai_choice = get_ai_choice(game_state)
    game_state[ai_choice] = symbol_map["ai"]

    if symbol_map["ai"] == 'X':
        draw_X(ai_choice, canvas)
    elif symbol_map["ai"] == 'O':
        draw_O(ai_choice, canvas)
    else:
        raise ValueError("Cannot draw symbol.")

    canvas.unbind("<Button-1>", tile_bindings[ai_choice])

def player_turn(player_choice : int,
                game_state : list[str],
                symbol_map : dict,
                canvas : Canvas,
                tile_bindings
                ):
    
    game_state[player_choice] = symbol_map["player"]
    
    if symbol_map["player"] == 'X':
        draw_X(player_choice, canvas)
    elif symbol_map["player"] == 'O':
        draw_O(player_choice, canvas)
    else:
        raise ValueError("Cannot draw symbol.")
    
    canvas.unbind("<Button-1>", tile_bindings[player_choice])

def minimax(game_state : list[str],
            score_map : dict, 
            turn : str, 
            player_symbol="O", 
            ai_symbol="X"
            ):
    
    if res := is_game_over(game_state):
        return score_map[res]
    
    scores = []
    for i in range(len(game_state)):
        if game_state[i] != " ":
            continue
        
        new_game_state = game_state.copy()
        if turn == "MAX":
            new_game_state[i] = ai_symbol
        else:
            new_game_state[i] = player_symbol
        scores.append(minimax(new_game_state, score_map, "MAX" if turn == "MIN" else "MIN"))
    
    return max(scores) if turn == "MAX" else min(scores)


def get_ai_choice(game_state : list[str], 
                  player_symbol='O', 
                  ai_symbol='X'
                  ):
    
    score_map = {player_symbol: -1, ai_symbol: 1, "Draw": 0}

    scores = []
    for i in range(len(game_state)):
        if game_state[i] != " ":
            continue
        
        new_game_state = game_state.copy()
        new_game_state[i] = ai_symbol
        scores.append((minimax(new_game_state, score_map, "MIN"), i))
    
    _, best_choice = max(scores, key=lambda x : x[0])

    return best_choice

