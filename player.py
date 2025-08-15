class Player:
    num_players = 0
    def __init__(self):
        self.name = ""
        self.symbol = ""
        Player.num_players += 1
    def get_info(self, player_num):
        while True:
            self.name = input(f"Player {player_num} name is : ")
            if self.name.isalpha():
                break
            else:
                print("invalid name")
        while True:
            self.symbol = input(f"{self.name} please enter your symbol : ")
            if (self.symbol.isalpha() and len(self.symbol) == 1):
                break
            else:
                print("invalid symbol, it must be one character")            
