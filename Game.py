from player import *
from menu import *
from board import *
import sys

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.menu = Menu()
        self.index = 0

    def start_game(self):
        if(self.menu.display_start_menu() == 2):
            sys.exit()
        while True:
            self.get_players()
            self.board.display_board()
            while True:
                self.play_turn()
                if(self.check_draw() or self.check_win()):
                    break
            if(self.menu.display_end_menu() == 2):
                sys.exit()
            self.board.reset_board()

    def play_turn(self):
        player = self.players[self.index]
        while True:
            num = input(f"player {player.name} choose from (1 - 9): ")
            if(num.isdigit()):
                if(int(num,10) in range(1,10) and self.board.update_board(int(num,10),player.symbol)):
                    break
                else:
                    print("invalid number, enter available number ")
            else:
                print("invalid value please enter interger number from (1 - 9)")
        self.index = ~self.index

    def check_win(self):
        for i in range(3):
            if(self.board.arr_symbols[i] == self.board.arr_symbols[i+3] == self.board.arr_symbols[i+6]):
                self.print_winner(self.board.arr_symbols[i])
                return True
        for i in range(3):
            if(self.board.arr_symbols[i*3] == self.board.arr_symbols[i*3+1] == self.board.arr_symbols[i*3+2]):
                self.print_winner(self.board.arr_symbols[i*3])
                return True
        if(self.board.arr_symbols[0] == self.board.arr_symbols[4] == self.board.arr_symbols[8]):
            self.print_winner(self.board.arr_symbols[0])
            return True
        if(self.board.arr_symbols[2] == self.board.arr_symbols[4] == self.board.arr_symbols[6]):
            self.print_winner(self.board.arr_symbols[2])
            return True


    def check_draw(self):
        for char in self.board.arr_symbols:
            if(char.isdigit()):
                return False
        print("Game Draw !!")
        return True
    
    def print_winner(self, symbol):
        if(self.players[0].symbol is symbol):
            print(f"{self.players[0].name} is Winner!!")
        else:
            print(f"{self.players[1].name} is Winner!!")

    def get_players(self):
        self.players = []
        for i in range(2):
            player = Player()
            player.get_info(i+1)
            self.players.append(player)