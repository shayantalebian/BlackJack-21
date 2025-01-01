import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

userCards = []
computerCards = []
userWin = False
computerWin = False
blackjack = True
cardGiving = True
sayN = False

# Card Chossing function
def cardChoose():
        return random.choice(cards)

while blackjack == True:
    gameOn = input("Do you want to play a game of BlackJack21? Type 'y' or 'n': ").lower()
    print("\n" * 200) # Clear the terminal
    userWin = False
    computerWin = False
    userCards = []
    computerCards = []

    if gameOn == "n":
        blackjack = False  
        break

    while len(userCards) < 2 and len(computerCards) < 2:
        userCards.append(cardChoose())
        computerCards.append(cardChoose())
    userScore = 0
    for card in userCards:
        userScore += card

    computerScore = 0
    for card in computerCards:
        computerScore += card

    print(logo)
    print(f"Your cards: {userCards}, current score: {userScore}")
    print(f"Compter's first card: {computerCards[0]}")

    while cardGiving == True:
        userChose = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if userChose == "y":
            userCards.append(cardChoose())
            userScore = 0
            for card in userCards:
                userScore += card
            if userScore > 21:
                userWin = False
                computerWin = True
            print(f"Your cards are: {userCards} and your score is: {userScore}")
            print(f"Comptuter's first card: {computerCards[0]}")

        elif userChose == "n":
            sayN = True
            while computerScore < 17:
                computerCards.append(cardChoose())
                computerScore = 0
                for card in computerCards:
                    computerScore += card
            

            print(f"Your final hand is: {userCards} and your score is: {userScore}")
            print(f"Computer's final hand is: {computerCards} and computer's final score is: {computerScore}")
            
            
        if (userWin == True or computerScore > 21) and userScore > computerScore:
            if sayN == False:
                print(f"Computer's final hand is: {computerCards} and computer's final score is: {computerScore}")
            print("You win!")
            break
        elif (computerWin == True or userScore > 21) and computerScore > userScore:
            if sayN == False:
                print(f"Computer's final hand is: {computerCards} and computer's final score is: {computerScore}")
            print("Computer won!")       
            break
        elif (userScore == computerScore) and (userScore <= 21 and computerScore <= 21):
            print("It's draw!!!")
            break

            
