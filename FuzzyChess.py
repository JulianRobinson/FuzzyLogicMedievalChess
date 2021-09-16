import base64
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image



# https://stackoverflow.com/questions/4954395/create-board-game-like-grid-in-python


class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=32, color1="gray", color2="blue"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        # added 200 to initialized width
        canvas_width = columns * size + 200
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        # need to work on resizing the pieces
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


# image comes from the silk icon set which is under a Creative Commons
# license. For more information see http://www.famfamfam.com/lab/icons/silk/
imagedata = '''
    R0lGODlhEAAQAOeSAKx7Fqx8F61/G62CILCJKriIHM+HALKNMNCIANKKANOMALuRK7WOVLWPV9eR
    ANiSANuXAN2ZAN6aAN+bAOCcAOKeANCjKOShANKnK+imAOyrAN6qSNaxPfCwAOKyJOKyJvKyANW0
    R/S1APW2APW3APa4APe5APm7APm8APq8AO28Ke29LO2/LO2/L+7BM+7BNO6+Re7CMu7BOe7DNPHA
    P+/FOO/FO+jGS+/FQO/GO/DHPOjBdfDIPPDJQPDISPDKQPDKRPDIUPHLQ/HLRerMV/HMR/LNSOvH
    fvLOS/rNP/LPTvLOVe/LdfPRUfPRU/PSU/LPaPPTVPPUVfTUVvLPe/LScPTWWfTXW/TXXPTXX/XY
    Xu/SkvXZYPfVdfXaY/TYcfXaZPXaZvbWfvTYe/XbbvHWl/bdaPbeavvadffea/bebvffbfbdfPvb
    e/fgb/Pam/fgcvfgePTbnfbcl/bfivfjdvfjePbemfjelPXeoPjkePbfmvffnvbfofjlgffjkvfh
    nvjio/nnhvfjovjmlvzlmvrmpvrrmfzpp/zqq/vqr/zssvvvp/vvqfvvuPvvuvvwvfzzwP//////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////yH+FUNyZWF0ZWQgd2l0aCBU
    aGUgR0lNUAAh+QQBCgD/ACwAAAAAEAAQAAAIzAD/CRxIsKDBfydMlBhxcGAKNIkgPTLUpcPBJIUa
    +VEThswfPDQKokB0yE4aMFiiOPnCJ8PAE20Y6VnTQMsUBkWAjKFyQaCJRYLcmOFipYmRHzV89Kkg
    kESkOme8XHmCREiOGC/2TBAowhGcAyGkKBnCwwKAFnciCAShKA4RAhyK9MAQwIMMOQ8EdhBDKMuN
    BQMEFPigAsoRBQM1BGLjRIiOGSxWBCmToCCMOXSW2HCBo8qWDQcvMMkzCNCbHQga/qMgAYIDBQZU
    yxYYEAA7
'''
# trying to find which data I need so it looks like this ^^^
# scratch that, don't need this
# whitePawnData = tk.PhotoImage("icons/whitePawn.png")
# img = base64.encodestring(whitePawnData.read())
# img = whitePawnData.load()
# print(img)

# https://stackoverflow.com/questions/6582387/image-resize-under-photoimage

#images.append(photoImg)
#text.image_create(INSERT, image=photoImg)




if __name__ == "__main__":
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    player1 = tk.PhotoImage(data=imagedata)

    # img = Image.open("icons/whitePawn.png")
    # img = img.resize((32, 32), Image.ANTIALIAS)

    # generating images for pieces
    whitePawn = ImageTk.PhotoImage(Image.open("icons/whitePawn.png").resize((32, 32), Image.ANTIALIAS))
    whiteKnight = ImageTk.PhotoImage(Image.open("icons/whiteKnight.png").resize((32, 32), Image.ANTIALIAS))
    whiteBishop = ImageTk.PhotoImage(Image.open("icons/whiteBishop.png").resize((32, 32), Image.ANTIALIAS))
    whiteRook = ImageTk.PhotoImage(Image.open("icons/whiteRook.png").resize((32, 32), Image.ANTIALIAS))
    whiteQueen = ImageTk.PhotoImage(Image.open("icons/whiteQueen.png").resize((32, 32), Image.ANTIALIAS))
    whiteKing = ImageTk.PhotoImage(Image.open("icons/whiteKing.png").resize((32, 32), Image.ANTIALIAS))
    # photoImg = tk.PhotoImage(data=img)
    # whitePawn = tk.PhotoImage(file="icons/whitePawn.png")

    blackPawn = ImageTk.PhotoImage(Image.open("icons/blackPawn.png").resize((32, 32), Image.ANTIALIAS))
    blackKnight = ImageTk.PhotoImage(Image.open("icons/blackKnight.png").resize((32, 32), Image.ANTIALIAS))
    blackBishop = ImageTk.PhotoImage(Image.open("icons/blackBishop.png").resize((32, 32), Image.ANTIALIAS))
    blackRook = ImageTk.PhotoImage(Image.open("icons/blackRook.png").resize((32, 32), Image.ANTIALIAS))
    blackQueen = ImageTk.PhotoImage(Image.open("icons/blackQueen.png").resize((32, 32), Image.ANTIALIAS))
    blackKing = ImageTk.PhotoImage(Image.open("icons/blackKing.png").resize((32, 32), Image.ANTIALIAS))

    # adding pieces to board
    board.addpiece("whiteAPawn", whitePawn, 6, 0)
    board.addpiece("whiteBPawn", whitePawn, 6, 1)
    board.addpiece("whiteCPawn", whitePawn, 6, 2)
    board.addpiece("whiteDPawn", whitePawn, 6, 3)
    board.addpiece("whiteEPawn", whitePawn, 6, 4)
    board.addpiece("whiteFPawn", whitePawn, 6, 5)
    board.addpiece("whiteGPawn", whitePawn, 6, 6)
    board.addpiece("whiteHPawn", whitePawn, 6, 7)

    board.addpiece("whiteARook", whiteRook, 7, 0)
    board.addpiece("whiteBKnight", whiteKnight, 7, 1)
    board.addpiece("whiteCBishop", whiteBishop, 7, 2)
    board.addpiece("whiteQueen", whiteQueen, 7, 3)
    board.addpiece("whiteKing", whiteKing, 7, 4)
    board.addpiece("whiteGKnight", whiteKnight, 7, 5)
    board.addpiece("whiteFBishop", whiteBishop, 7, 6)
    board.addpiece("whiteHRook", whiteRook, 7, 7)

    board.addpiece("blackAPawn", blackPawn, 1, 0)
    board.addpiece("blackBPawn", blackPawn, 1, 1)
    board.addpiece("blackCPawn", blackPawn, 1, 2)
    board.addpiece("blackDPawn", blackPawn, 1, 3)
    board.addpiece("blackEPawn", blackPawn, 1, 4)
    board.addpiece("blackFPawn", blackPawn, 1, 5)
    board.addpiece("blackGPawn", blackPawn, 1, 6)
    board.addpiece("blackHPawn", blackPawn, 1, 7)

    board.addpiece("blackARook", blackRook, 0, 0)
    board.addpiece("blackBKnight", blackKnight, 0, 1)
    board.addpiece("blackCBishop", blackBishop, 0, 2)
    board.addpiece("blackQueen", blackQueen, 0, 3)
    board.addpiece("blackKing", blackKing, 0, 4)
    board.addpiece("blackGKnight", blackKnight, 0, 5)
    board.addpiece("blackFBishop", blackBishop, 0, 6)
    board.addpiece("blackHRook", blackRook, 0, 7)

    board.placepiece("whiteDPawn", 4, 3)

    root.mainloop()
