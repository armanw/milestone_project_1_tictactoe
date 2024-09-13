from board import Board
from decision import Decision
from tkinter import Tk, messagebox, Entry, Label, Button, Canvas, CENTER, mainloop
import abc


class Renderer(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def display_board(game_board: Board):
        pass

    @staticmethod
    @abc.abstractmethod
    def ask_question(question: Decision) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def display_message(message: str):
        pass


class ConsoleRenderer(Renderer):
    @staticmethod
    def display_board(game_board: Board):
        # show Board object, no matter what it is
        separator = '--- | --- | ---'
        line = ' {}  |  {}  |  {} '
        print(line.format(
            game_board.get_symbol_at(1, 1),
            game_board.get_symbol_at(1, 2),
            game_board.get_symbol_at(1, 3)
        ))
        print(separator)
        print(line.format(
            game_board.get_symbol_at(2, 1),
            game_board.get_symbol_at(2, 2),
            game_board.get_symbol_at(2, 3)
        ))
        print(separator)
        print(line.format(
            game_board.get_symbol_at(3, 1),
            game_board.get_symbol_at(3, 2),
            game_board.get_symbol_at(3, 3)
        ))

    @staticmethod
    def ask_question(asked_question: Decision) -> str:
        answer = input(asked_question.question)

        while not asked_question.validate(answer):
            # while asked_question...== FALSE
            print(asked_question.error_msg)
            answer = input(asked_question.question)

        return answer.lower()

    @staticmethod
    def display_message(message: str):
        print(message)


class FancyRenderer(Renderer):
    answer = ""
    root = None
    running = False

    @staticmethod
    def display_message(message: str):
        messagebox.showinfo(message=message)

    @staticmethod
    def ask_question(question: Decision):
        w = Tk()
        l = Label(w, text=question.question)
        l.pack()
        inp = Entry(w)
        inp.pack()
        inp.focus_set()

        def clbck():
            a = inp.get()
            if not question.validate(a):
                messagebox.showerror(message=question.error_msg)
            else:
                FancyRenderer.answer = a
                w.destroy()

        b = Button(w, text="OK", width=10, command=clbck)
        b.pack()

        mainloop()

        return FancyRenderer.answer

    @staticmethod
    def display_board(board: Board):
        if FancyRenderer.running:
            FancyRenderer.root.destroy()
        FancyRenderer.root = Tk()
        FancyRenderer.root.geometry('400x400')
        canvas = Canvas(FancyRenderer.root, width=300, height=300, bg='white')
        canvas.pack(anchor=CENTER, expand=True)

        canvas.create_line((100, 0), (100, 300), width=5)
        canvas.create_line((200, 0), (200, 300), width=5)
        canvas.create_line((0, 100), (300, 100), width=5)
        canvas.create_line((0, 200), (300, 200), width=5)

        for row in range(1, 4):
            for col in range(1, 4):
                symb = board.get_symbol_at(row, col)

                off = 35
                tlc_x = 100 * (col - 1) + off
                tlc_y = 100 * (row - 1) + off

                brc_x = 100 * (col - 1) + 2 * off
                brc_y = 100 * (row - 1) + 2 * off

                if symb == 'x':
                    canvas.create_line((tlc_x, tlc_y), (brc_x, brc_y), width=3)
                    canvas.create_line((brc_x, tlc_y), (tlc_x, brc_y), width=3)
                elif symb == 'o':
                    canvas.create_line((tlc_x, tlc_y), (brc_x, tlc_y), width=3)
                    canvas.create_line((tlc_x, tlc_y), (tlc_x, brc_y), width=3)
                    canvas.create_line((brc_x, brc_y), (tlc_x, brc_y), width=3)
                    canvas.create_line((brc_x, brc_y), (brc_x, tlc_y), width=3)
        mainloop()