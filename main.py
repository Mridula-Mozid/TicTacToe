# 1. Enter player names x
#2. Assign signs x
#3. Give instructions & the board x
#4. Start the game x
#5. Give instructions accordingly & player 01 will move first x
#6. place the position and show the board 
#7. player 02 will move next x
#8. make sure the position is empty 
#9. place the position and show the board
#10. check for win or draw & repeat or end the game

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


def main():
  print("Welcome to The Tic-Tac-Toe Game!")
  player01 = input("Enter player 01 name: ")
  player02 = input("Enter player 02 name: ")

  print(f"\nWelcome {player01} & {player02}")
  print(f"{player01} is X AND {player02} is O")

  print(instuctions)

  current_player = player01
  current_symbol = 'X'
  

  for i in range(1,9):
    if i % 2 != 0:
      digit = int(input(f"{current_player}({current_symbol}) enter your position: "))
      if board[digit] != 'X' or 'O' and digit <= 9 and digit != 0:
        board[digit-1] = 'X'
        print(board)
        current_player = player02
        current_symbol = 'O'
      else:
         print("Your input is invalid. Please enter unoccupied digits from 1 through 9")
         i = i-1

    elif i % 2 == 0:
      digit = int(input(f"{current_player}({current_symbol}) enter your position: "))
      if board[digit] != 'X' or 'O' and digit <= 9:
        board[digit-1] = 'O'
        print(board)
        current_player = player01
        current_symbol = 'X'
      else:
         print("Your input is invalid. Please enter unoccupied digits from 1 through 9 ONLY")
         i = i-1
    
    else:
      print("Your input is invalid. Please enter unoccupied digits from 1 through 9")

main()


