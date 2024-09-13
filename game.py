from typing import List, Any, Type

from decision import Decision
from renderer import Renderer
from player import Player
from board import Board


class Game:

    def __init__(self, renderer_type: Type[Renderer]):
        self.__game_board: Board = Board()
        self.__player1: Player = Player()
        self.__player2: Player = Player()
        self.__players: List[Player] = [self.__player1, self.__player2]
        self.__current_player_index: int = 0

        self.__renderer: Type[Renderer] = renderer_type
        # choosing rendered class

    def __assign_symbols_to_players(self):

        symbol_question = Decision(
            question="Player1 - Choose symbol o or x: ",
            validation_rule=r'[oxOX]',
            error_msg="You can choose only X or O"
        )
        # ask Player1 to choose symbol

        chosen_symbol = self.__renderer.ask_question(symbol_question)

        self.__player1.chosen_symbol = chosen_symbol
        self.__player2.chosen_symbol = 'x' if chosen_symbol == 'o' else 'o'

    def __run_player_turn(self, coordinate_question: Decision):
        self.__renderer.display_message(
            f'Player{self.__current_player_index + 1} turn ({self.__players[self.__current_player_index].chosen_symbol})'
        )

        # check if chosen cell is empty:
        cell_empty = False
        while not cell_empty:

            chosen_coordinates = self.__renderer.ask_question(coordinate_question)
            chosen_x = int(chosen_coordinates[1])
            chosen_y = int(chosen_coordinates[3])

            # check if cell in provided coordinates is empty
            cell_empty = self.__game_board.get_symbol_at(chosen_x, chosen_y) == ' '

            # if cell is empty, then allow to put symbol
            if cell_empty:

                self.__game_board.put_symbol(
                    symbol=self.__players[self.__current_player_index].chosen_symbol,
                    row_x=chosen_x,
                    column_y=chosen_y
                )
            else:
                self.__renderer.display_message("This cell is already taken, choose another")

    def run(self):

        self.__assign_symbols_to_players()

        coordinate_question = Decision(
            question="Provide coordinates as (x,y): ",
            validation_rule=r'\([1-3],[1-3]\)',
            error_msg="Provide coordinates in correct format (x,y): "
        )

        while not self.__game_board.is_full():

            self.__renderer.display_board(self.__game_board)
            self.__run_player_turn(coordinate_question)

            if self.__game_board.has_3_in_line():
                self.__renderer.display_message(f"Congrats Player {self.__current_player_index + 1}, you won!")
                # stop while loop:
                break

            # change player index:
            self.__current_player_index = 1 if self.__current_player_index == 0 else 0

        # last display of board
        self.__renderer.display_board(self.__game_board)
