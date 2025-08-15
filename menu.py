import os # use to control terminal
import sys # used for terminate program

class Menu:
    def __init__(self):
        pass

    def display_start_menu(self):
        os.system("cls")
        print("1.Start game\n","2.Quit game\n",sep='')
        return Menu.get_input()

    def display_end_menu(self):
        print("1.Play again\n","2.Quit game",sep='')
        return Menu.get_input()

    @(staticmethod)
    def get_input():
        while True:
            tmp = input("enter number (1 or 2): ")
            if(tmp.isdigit()):
                if(int(tmp,10) in [1,2]):
                    break
                else:
                    print("invalid number")
            else:
                print("invalid number ")
        return int(tmp,10)
        