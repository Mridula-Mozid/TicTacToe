# 1. Enter player names x
#2. Assign signs x
#3. Give instructions & the board x
#4. Start the game x
#5. Give instructions accordingly & player 01 will move first x
#6. place the position and show the board x
#7. player 02 will move next x
#8. make sure the position is empty x
#9. place the position and show the board x
#10. check for win or draw & repeat or end the game x

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


def check_winner(player_name, symbol):
    if (board[0] == board[1] == board[2] == symbol) or \
       (board[3] == board[4] == board[5] == symbol) or \
       (board[6] == board[7] == board[8] == symbol) or \
       (board[0] == board[3] == board[6] == symbol) or \
       (board[1] == board[4] == board[7] == symbol) or \
       (board[2] == board[5] == board[8] == symbol) or \
       (board[0] == board[4] == board[8] == symbol) or \
       (board[2] == board[4] == board[6] == symbol):
        print(f"Congratulation! {player_name} WON!!!")
        quit()
    return False


def main():
  print("Welcome to The Tic-Tac-Toe Game!")
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
        check_winner(current_player, 'X')
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
        check_winner(current_player, 'O')
        current_player = player01
        current_symbol = 'X'
        i += 1
      else:
         print("Your input is invalid. Please enter unoccupied digits from 1 through 9 ONLY")
  print("It's a draw!!!")
  input("Press Enter to exit!")
main()


