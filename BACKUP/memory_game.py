import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')



class Board():
    
    def __init__(self, width = 5, heigth = 4):
        self.width = width
        self.heigth = heigth

        self.hidden_board = []
        self.letters_board = []


        self.generate_boards()
        

    # def insert_columns_rows_labels(self):
    #     row_id = 1
    #     for row_index in range(1, self.height+1):
    #         self.letters_board[row_index][0] = row_id
    #         self.hidden_board[row_index][0] = row_id
    #         row_id += 1
        
    #     column_id = 0 # we use alphabet string variable
    #     for column_index in range(1, self.width):
    #         self.letters_board[0][column_index] = alphabet[column_id]
    #         self.hidden_board[0][column_index] = alphabet[column_id]
    #         column_id += 1

        
        
    def generate_boards(self) -> None:
        # first hidden board shown to user while playing 
        self.hidden_board = [['#' for row in range(0, self.heigth)] for column in range(0, self.width)]

        # new board with letters to guess
        self.letters_board = [['' for row in range(0, self.heigth)] for column in range(0, self.width)]
        #self.insert_columns_rows_labels()

        # fill letters board with random letters on random cells
        alphabet_list = []
        alphabet_list[:] = alphabet
        
        available_space_for_letters = self.width * self.heigth
        while available_space_for_letters > 0:
            random_letter = random.choice(alphabet_list)
            alphabet_list.remove(random_letter)
            available_space_for_letters -= 2
            
            # draw 2 empty space from letters_board
            drawn_cells_for_letter = Coordinates.get_random_available_cell(self)
            if not drawn_cells_for_letter == False:
                row = 0
                column = 1
                cell_1 = drawn_cells_for_letter[0]
                cell_2 = drawn_cells_for_letter[1]
                self.letters_board[cell_1[row]][cell_1[column]] = random_letter
                self.letters_board[cell_2[row]][cell_2[column]] = random_letter

    def display_board(self) -> None:
        for row in self.hidden_board:
            for cell in row:
                print(cell," ", end="")
            print("")

            



    def show_board(self) -> None:
        pass


class Coordinates:
    def __init__(self):
        pass

    def get_random_available_cell(board: Board) -> list or bool:
        available_empty_cells = []
        for row in range(0, board.heigth):
            for column in range(0, board.width):
                if board.letters_board[row][column] == '':
                    available_empty_cells.append([row, column])
        
        if len(available_empty_cells) >= 2:
            random_cell_1 = random.choice(available_empty_cells)
            random_cell_2 = random.choice(available_empty_cells)

            return [random_cell_1,random_cell_2]
        else:
            return False
                    

             


class Game:
    game_levels = {'level easy':1, 'level medium':2, 'level hard':3}
    game_state = {'main_menu':1, 'initiate':2, 'play':3, 'exit_program':5}

    def __init__ (self):
        self.current_game_state = Game.game_state['main_menu']
        self.chosen_level = ""

        self.exit_program = False

        self.board = Board()

    def play(self) -> None:

        while not self.exit_program:
            if self.current_game_state == Game.game_state['main_menu']:
                self.show_menu()
                self.current_game_state = Game.game_state['initiate']

            elif self.current_game_state == Game.game_state['initiate']:
                if self.chosen_level == Game.game_levels['level easy']:
                    #             When picked the Easy difficulty level, the board's size should be 5x4
                    self.board = Board(5,4)
                elif self.chosen_level == Game.game_levels['level medium']:
                    #             When picked the Medium difficulty level, the board's size should be 5x6
                    self.board = Board(5,6)
                else: # self.chosen_level == game_levels['level hard']:
                    #             When picked the Hard difficulty level, the board's size should be 5x10
                    self.board = Board(5,10)
                self.current_game_state = Game.game_state['play']

            elif self.current_game_state == Game.game_state['play']:
                end_game = False
                quit_game = False
                while not end_game or not quit_game:
                    console_clear()
                    self.board.display_board()
                    
                    
                    quit_game = True
                    input("press any key..")
                self.current_game_state == Game.game_state['main_menu']

            elif self.current_game_state == Game.game_state['exit_program']:
                    quit_game
                    self.quit()

    

    def show_menu(self) -> None:
        console_clear()
        print('Welcome to Memory Game!')
        self.chosen_level = self.ask_user_for_level()
        
    
    def ask_user_for_level(self) -> int:
            is_user_input_corret = False
            while not is_user_input_corret:
                user_input = input("Choose level 1-easy / 2-medium / 3-hard: ")
                is_user_input_corret = self.is_asked_user_level_correct(user_input)
                if is_user_input_corret == False:
                    print("Error: Not valid level")
                else: #is_user_input_correct == True
                    is_user_input_corret = True

            return int(user_input)
                
    def is_asked_user_level_correct(self, user_input: str) -> bool:
        try:
            is_user_input_corret = int(user_input)
            return True
        except:
            return False
    

    


    def game_over(self) -> None:
        pass

    def quit(self) -> None:
        pass


      


def main():
    new_game = Game()
    new_game.play()


   

if __name__ == "__main__":
    main()