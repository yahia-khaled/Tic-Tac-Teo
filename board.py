import os
class Board:
    def __init__(self):
        self.initialize_array()
    
    def get_list(self):
        print(self.arr_symbols)

    def display_board(self):
        os.system("cls")
        for i in range(3):
            print(f"{self.arr_symbols[i*3]} | {self.arr_symbols[i*3+1]} | {self.arr_symbols[i*3+2]}")
            if i != 2:
                print(9 * "-")  

    def update_board(self, num, symb):
        if self.arr_symbols[num-1].isalpha():
            self.display_board()
            return False
        else:
            self.arr_symbols[num-1] = symb
            self.display_board()
            return True

    def reset_board(self):
        self.initialize_array()
        self.display_board()

    def initialize_array(self):
        self.arr_symbols = []
        for i in range(9):
            self.arr_symbols.append(str(i+1))

# use list comprehension                self.arr_symbols = [str(i) for i in range (1,10)]

# join with list elements           "sep_character".join(list[range_of_elements])


