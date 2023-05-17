# import random module
import random
# print multiline instruction
# performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissors -> Rock wins \n"
        + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissor \n")

    comp1_choice = random.randint(1, 3)

    if comp1_choice == 1:
        choice_name = 'Rock'
    elif comp1_choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('Computer_1 choice is \n', choice_name)
    print('Now its Computers_2 Turn....')

    comp2_choice = random.randint(1, 3)

    while comp2_choice == comp1_choice:
        comp2_choice = random.randint(1, 3)

    if comp2_choice == 1:
        comp_choice_name = 'Rock'
    elif comp2_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'
    print("Computer_2 choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    # we need to check of a draw
    if comp1_choice == comp2_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    # condition for winning
    if (comp1_choice == 1 and comp2_choice == 2):
        print('paper wins =>', end="")
        result = 'Paper'
    elif (comp1_choice == 2 and comp2_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (comp1_choice == 1 and comp2_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (comp1_choice == 3 and comp2_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'Rock'

    if (comp1_choice == 2 and comp2_choice == 3):
        print('Scissors wins =>', end="")
        result = 'Scissor'
    elif (comp1_choice == 3 and comp2_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Scissor'
    # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== computer_1 wins ==>")
    else:
        print("<== Computer_2 wins ==>")
    print("Do you want to play again? (1/0)")
    # if user input n or N then condition is Trueans = input().lower
    flag = int(input())
    if flag == 0:
        break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")
