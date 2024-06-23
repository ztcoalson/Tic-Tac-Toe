from tkinter import Tk, Canvas, IntVar, Event, CENTER
from itertools import product

def print_result(canvas : Canvas, result : str, symbol_map : dict):
    if result == "Draw":
        text = "It's a draw! (Makes sense, you literally cannot win)"
    elif result == symbol_map["ai"]:
        text = "The AI won! (cmon...)"
    else:
        text = "You won... by cheating."
    
    canvas.create_text(250, 75, text=text, anchor=CENTER)

def draw_X(tile : int, canvas : Canvas):
    x, y = (tile % 3) * 100 + 150, (tile // 3) * 100 + 150
    half_size = 30
    canvas.create_line(x - half_size, y - half_size, x + half_size, y + half_size, width=3, fill="black")
    canvas.create_line(x - half_size, y + half_size, x + half_size, y - half_size, width=3, fill="black")

def draw_O(tile : int, canvas : Canvas):
    x, y = (tile % 3) * 100 + 150, (tile // 3) * 100 + 150
    radius = 40
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="black", fill="", width=3)

def build_gui():

    def on_tile_click(event : Event):
        tile = int(event.widget.gettags("current")[0])
        curr_tile.set(tile)

    window = Tk()

    window.title("Tic-Tac-Toe")
    window.geometry('500x500')

    canvas=Canvas(window, width=500, height=500)
    canvas.pack()

    canvas.create_line(100,200,400,200, fill="black", width=3)
    canvas.create_line(100,300,400,300, fill="black", width=3)
    canvas.create_line(200,400,200,100, fill="black", width=3)
    canvas.create_line(300,400,300,100, fill="black", width=3)

    tile_bindings = {}
    x1, y1, x2, y2 = 10, 10, 90, 90
    for i, (y,x) in enumerate(product((100,200,300), (100,200,300))):
        rect = canvas.create_rectangle(x1+x, y1+y, x2+x, y2+y, outline="", fill="", tags=str(i))
        binding = canvas.tag_bind(rect, "<Button-1>", on_tile_click)
        tile_bindings[i] = binding

    curr_tile = IntVar()

    return window, canvas, curr_tile, tile_bindings
    