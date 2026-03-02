import random


instuctions = """

   1  | 2 | 3
  ----|---|---
   4  | 5 | 6
  ----|---|---
   7  | 8 | 9
This is your board.


Player 01 will make the move first and then player 02. 
Afterwards, it'll keep repeating until someone wins or it's a draw.
Enter the assigned placeholder number of the place, where you want to put the sign.

So without further ado, let's start.

  """

board = ['1', '2', '3', 
         '4', '5', '6',
         '7', '8', '9']


def print_board():
    print(f"""
 {board[0]} | {board[1]} | {board[2]}
---|---|---
 {board[3]} | {board[4]} | {board[5]}
---|---|---
 {board[6]} | {board[7]} | {board[8]}""")


def check_winner(player_name, symbol, check_only=False):
    is_winner = False
    if (board[0] == board[1] == board[2] == symbol) or \
       (board[3] == board[4] == board[5] == symbol) or \
       (board[6] == board[7] == board[8] == symbol) or \
       (board[0] == board[3] == board[6] == symbol) or \
       (board[1] == board[4] == board[7] == symbol) or \
       (board[2] == board[5] == board[8] == symbol) or \
       (board[0] == board[4] == board[8] == symbol) or \
       (board[2] == board[4] == board[6] == symbol):
        is_winner = True
    
    if is_winner and not check_only:
        print(f"Congratulation! {player_name} WON!!!")
        input("Press Enter to exit...")
        quit()
        
    return is_winner


def minimax(board, depth, is_maximizing):
    if check_winner("Computer", 'O', check_only=True):
        return 10 - depth
    if check_winner("Player", 'X', check_only=True):
        return depth - 10
    
    empty_spots = [idx for idx, val in enumerate(board) if val not in ['X', 'O']]
    
    if not empty_spots:
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for index in empty_spots:
            original_val = board[index]
            board[index] = 'O'
            score = minimax(board, depth + 1, False)
            board[index] = original_val
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for index in empty_spots:
            original_val = board[index]
            board[index] = 'X'
            score = minimax(board, depth + 1, True)
            board[index] = original_val
            best_score = min(score, best_score)
        return best_score


def main():
    print("Welcome to The Tic-Tac-Toe Game!")
    preference = input("Do you want to play against a human or computer? Type 'human' or 'computer': ")
    
    if preference.lower() == 'human':
        print("Welcome to the human vs human Mode! ")
        player01 = input("Enter player 01 name: ")
        player02 = input("Enter player 02 name: ")

        print(f"\nWelcome {player01} & {player02}")
        print(f"{player01} is X AND {player02} is O")

        print(instuctions)

        current_player = player01
        current_symbol = 'X'

        i = 1
        while i <= 9:
            if i % 2 != 0:
                digit = int(input(f"{current_player}({current_symbol}) enter your position: "))
                if digit > 0 and digit <= 9 and board[digit-1] != 'X' and board[digit-1] != 'O':
                    board[digit-1] = 'X'
                    print_board()
                    check_winner(current_player, current_symbol)
                    current_player = player02
                    current_symbol = 'O'
                    i += 1
                else:
                    print("Your input is invalid. Please enter unoccupied digits from 1 through 9")

            else:
                digit = int(input(f"{current_player}({current_symbol}) enter your position: "))
                if digit > 0 and digit <= 9 and board[digit-1] != 'X' and board[digit-1] != 'O':
                    board[digit-1] = 'O'
                    print_board()
                    check_winner(current_player, current_symbol)
                    current_player = player01
                    current_symbol = 'X'
                    i += 1
                else:
                    print("Your input is invalid. Please enter unoccupied digits from 1 through 9 ONLY")
        
        print("It's a draw!!!")
        input("Press Enter to exit!")
    
    else:
        print("Welcome to the Computer Mode! ")
        difficulty = int(input("Choose your difficulty level:\n" \
        "1. Easy (Enter 1)\n" \
        "2. Medium (Enter 2)\n" \
        "3. Hard (Enter 3): \n"))
        
        while difficulty > 0 and difficulty < 4: 
          if difficulty == 1:
              print("You have selected Easy mode.")

              player01 = input("Enter player name: ")
              print(f"Welcome {player01}. You are playing against the computer. \nYou are X and the computer is O.")
              print(instuctions)

              current_player = player01
              current_symbol = 'X'

              i = 1
              while i<=9:
                if i % 2 != 0:
                    digit = int(input(f"{current_player}({current_symbol}) enter your position: "))

                    if digit > 0 and digit <= 9 and board[digit-1] != 'X' and board[digit-1] != 'O':
                        board[digit-1] = 'X'
                        print_board()
                        check_winner(current_player, 'X')
                        current_player = "Computer"
                        current_symbol = 'O'
                        i += 1
                    else:
                        print("Your input is invalid. Please enter unoccupied digits from 1 through 9")

                else:
                    index = random.randint(1, 9)
                    if index > 0 and index <= 9 and board[index-1] not in ['X', 'O']:
                        print(f"Computer chooses position {index}")
                        board[index-1] = 'O'
                        print_board()
                        check_winner(current_player, 'O')
                        current_player = player01
                        current_symbol = 'X'
                        i += 1 
                    else:
                        continue
              
              print("It's a draw!!!")
              input("Press Enter to exit!")
              break

          elif difficulty == 2:
              print("You have selected Medium mode.")

              player01 = input("Enter player name: ")
              print(f"Welcome {player01}. You are playing against the computer. \nYou are X and the computer is O.")
              print(instuctions)

              current_player = player01
              current_symbol = 'X'

              i = 1
              while i<=9:
                if i % 2 != 0:
                    digit = int(input(f"{current_player}({current_symbol}) enter your position: "))

                    if digit > 0 and digit <= 9 and board[digit-1] != 'X' and board[digit-1] != 'O':
                        board[digit-1] = 'X'
                        print_board()
                        check_winner(current_player, current_symbol)
                        current_player = "Computer"
                        current_symbol = 'O'
                        i += 1
                        search = True
                    else:
                        print("Your input is invalid. Please enter unoccupied digits from 1 through 9")

                else:
                    while search:
                      for item in board:
                          i=1
                          while i <= 9:
                              check_winner("Computer", 'O', check_only=True)
                              if check_winner("Computer", 'O', check_only=True) == True:
                                  index = board.index(item)
                                  print(f"Computer chooses position {index+1}")
                                  board[index] = 'O'
                                  print_board()
                                  check_winner(current_player, 'O')
                                  current_player = player01
                                  current_symbol = 'X'
                                  i += 1 
                                  
                                  break
                              
                              else:
                                  continue
  
                            
                      while i == 10:
                          index = random.randint(1, 9)
                          if index > 0 and index <= 9 and board[index-1] not in ['X', 'O']:
                              print(f"Computer chooses position {index}")
                              board[index-1] = 'O'
                              print_board()
                              check_winner(current_player, 'O')
                              current_player = player01
                              current_symbol = 'X'
                              i += 1 
                          else:
                              continue
              
              print("It's a draw!!!")
              input("Press Enter to exit!")
              break

              
          elif difficulty == 3:
              print("You have selected Hard mode.")
              
              player01 = input("Enter player name: ")
              print(f"Welcome {player01}. You are playing against the computer. \nYou are X and the computer is O.")
              print(instuctions)

              current_player = player01
              current_symbol = 'X'

              i = 1
              while i <= 9:
                  if i % 2 != 0:
                      # Human Turn
                      try:
                          digit = int(input(f"{current_player}({current_symbol}) enter your position: "))
                          if digit > 0 and digit <= 9 and board[digit-1] not in ['X', 'O']:
                              board[digit-1] = 'X'
                              print_board()
                              check_winner(current_player, 'X')
                              current_player = "Computer"
                              current_symbol = 'O'
                              i += 1
                          else:
                              print("Your input is invalid. Please enter unoccupied digits from 1 through 9")
                      except ValueError:
                          print("Invalid input. Please enter a number.")
                  else:
                      # Computer Turn (Hard - Minimax)
                      best_score = -float('inf')
                      move_index = -1
                      
                      empty_spots = [idx for idx, val in enumerate(board) if val not in ['X', 'O']]
                      
                      # Minimax to find best move
                      for index in empty_spots:
                          board[index] = 'O'
                          score = minimax(board, 0, False)
                          board[index] = str(index + 1) # Undo move
                          
                          if score > best_score:
                              best_score = score
                              move_index = index
                      
                      # Make the best move
                      print(f"Computer chooses position {move_index + 1}")
                      board[move_index] = 'O'
                      print_board()
                      check_winner(current_player, 'O')
                      
                      current_player = player01
                      current_symbol = 'X'
                      i += 1
              
              print("It's a draw!!!")
              input("Press Enter to exit!")
              break
        else:
          print("Invalid input. Please enter 1, 2, or 3.")

main()


