rock = '''
1 ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
2 PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
3 SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lizard = '''
4 LIZARD
    _______
---'   ____)____
          ______)
       __________)
      _________)
---.__(___)
'''
spock = '''
5 SPOCK
    _______
---'   ____)____
          ______)
          _______)
          |_____
         _______)
---.__________)
'''
import random
gameRound = 1
playerScore= 0
computerScore = 0
listOf = [rock, paper, scissors, lizard, spock]

print("Welcome to the game.")
rules = "Scissors cuts paper.\nPaper covers rock.\nRock crushes lizard.\nLizard poisons Spock.\nSpock smashes scissors.\nScissors decapitates lizard.\nLizard eats paper.\nPaper disproves Spock.\nSpock vaporizes rock.\nRock crushes scissors."

print("Enter 0 to see the rules\nEnter 1 for rock \nEnter 2 for papers \nEnter 3 for scissors \nEnter 4 for lizard \nEnter 5 for spock")


while gameRound <= 5 or (computerScore == 0 and playerScore == 0):

 print(f"-------------- Round: {gameRound} --------------")
 print(f"****** Scoreboard ******\nPlayer: {playerScore}\nComputer: {computerScore}")
 computerChoiceNum = random.randint(0,4)

 while True:
     try:
        validate = int(input("1 Rock, 2 Paper, 3 Scissors, 4 Lizard, 5 Spock!\n"))

        if validate < 0 or validate > 5:
            print("Unacceptable number. Enter numbers between 0-5 (included)")
        else:
            break
     except ValueError:
         print("Enter 0 to see the rules\nEnter 1 for rock \nEnter 2 for papers \nEnter 3 for scissors \nEnter 4 for lizard \nEnter 5 for spock")



 userChoiceNum = validate - 1

 if userChoiceNum == -1:
  print(rules)
  continue

 gameRound += 1
 computerChoiceShape = listOf[computerChoiceNum]
 userChoiceShape = listOf[userChoiceNum]
 print("Your move:")
 print(userChoiceShape)
 print("Opponent's move:")
 print(computerChoiceShape)


 if userChoiceNum == computerChoiceNum:
  print("TIE. NO POINTS.")
  continue

        # paper - rock
 if (userChoiceNum  == 1 and computerChoiceNum == 0) or (userChoiceNum == 0 and computerChoiceNum == 1):
    print("Paper covers rock.")
    if userChoiceNum == 0:
        computerScore += 1
    else:
        playerScore += 1

         # rock - scissors
 if (userChoiceNum  == 2 and computerChoiceNum == 0) or (userChoiceNum == 0 and computerChoiceNum == 2):
     print("Rock smashes scissors.")
     if userChoiceNum == 0:
         playerScore += 1
     else:
         computerScore += 1

         # rock - lizard
 if (userChoiceNum  == 3 and computerChoiceNum == 0) or (userChoiceNum == 0 and computerChoiceNum == 3):
     print("Rock crushes lizard.")
     if userChoiceNum == 0:
         playerScore += 1
     else:
         computerScore += 1

         # rock - spock
 if (userChoiceNum  == 0 and computerChoiceNum == 4) or (userChoiceNum == 4 and computerChoiceNum == 0):
     print("Spock vaporizes rock.")
     if userChoiceNum == 0:
         computerScore += 1
     else:
         playerScore += 1

         # paper - scissors
 if (userChoiceNum  == 2 and computerChoiceNum == 1) or (userChoiceNum == 1 and computerChoiceNum == 2):
     print("Scissors cut paper.")
     if userChoiceNum == 1:
         computerScore += 1
     else:
         playerScore += 1

         # paper - lizard
 if (userChoiceNum  == 3 and computerChoiceNum == 1) or (userChoiceNum == 1 and computerChoiceNum == 3):
     print("Lizard eats paper.")
     if userChoiceNum == 1:
         computerScore += 1
     else:
         playerScore += 1

         # paper - spock
 if (userChoiceNum  == 4 and computerChoiceNum == 1) or (userChoiceNum == 1 and computerChoiceNum == 4):
     print("Paper disproves Spock.")
     if userChoiceNum == 1:
         playerScore += 1
     else:
         computerScore += 1

         # scissors - lizard
 if (userChoiceNum  == 2 and computerChoiceNum == 3) or (userChoiceNum == 3 and computerChoiceNum == 2):
     print("Scissors decapitates lizard.")
     if userChoiceNum == 2:
         playerScore += 1
     else:
         computerScore += 1

         # scissors - spock
 if (userChoiceNum  == 2 and computerChoiceNum == 4) or (userChoiceNum == 4 and computerChoiceNum == 2):
     print("Spock smashes scissors.")
     if userChoiceNum == 2:
         computerScore += 1
     else:
         playerScore += 1

         # lizard - spock
 if (userChoiceNum  == 3 and computerChoiceNum == 4) or (userChoiceNum == 4 and computerChoiceNum == 3):
     print("Lizard poisons Spock.")
     if userChoiceNum == 3:
         playerScore += 1
     else:
         computerScore += 1

print("GAME OVER")
print(f"****** Scoreboard ******\nPlayer: {playerScore}\nComputer: {computerScore}")
if(computerScore < playerScore):
    print("YOU WON")
else:
    print("YOU LOSE")