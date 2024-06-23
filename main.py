from gui import build_gui, print_result
from game_functions import is_game_over, player_turn, ai_turn

SYMBOL_MAP = {"player": 'O', "ai": 'X'}

if __name__ == "__main__":
    window, canvas, curr_tile, tile_bindings = build_gui()
    game_state = [" "] * 9
    
    turn = "ai"
    while not (res := is_game_over(game_state)):
        if turn == "ai":
            turn = "player"
            ai_turn(game_state, SYMBOL_MAP, canvas, tile_bindings)
        else:
            turn = "ai"
            window.wait_variable(curr_tile)
            player_choice = curr_tile.get()
            player_turn(player_choice, game_state, SYMBOL_MAP, canvas, tile_bindings)

        if res := is_game_over(game_state):
            break
    
    print_result(canvas, res, SYMBOL_MAP)
    window.mainloop()

