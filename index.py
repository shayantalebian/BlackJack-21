import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = True

# Card Chossing function
def cardChoose():
        return random.choice(cards)

while blackjack == True:
    gameOn = input("Do you want to play a game of BlackJack21? Type 'y' or 'n': ").lower()
    print("\n" * 200) # Clear the terminal
    userCards = []
    computerCards = []
    cardGiving = True

    if gameOn == "n":
        blackjack = False  
        break

    while len(userCards) < 2 and len(computerCards) < 2:
        userCards.append(cardChoose())
        computerCards.append(cardChoose())
    userScore = sum(userCards)
        
    computerScore = sum(computerCards)
    if 11 in userCards or 11 in computerCards:
        if userCards[0] == 11 and userCards[1] == 11:
            userCards[1] = 1
        elif computerCards[0] == 11 and computerCards[1] == 11:
            computerCards[1] = 1

    print(logo)
    print(f"Your cards: {userCards}, current score: {userScore}")
    print(f"Compter's first card: {computerCards[0]}")

    while cardGiving == True:
        userChose = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if userChose == "y":
            userCards.append(cardChoose())
            userScore = sum(userCards)
            if userScore > 21:
                if 11 in userCards:
                    userCards[userCards.index(11)] = 1
                    userScore = sum(userCards)
                    print(f"Your cards are: {userCards} and your score is: {userScore}")
                    print(f"Compter's first card: {computerCards[0]}")
                else:
                    print(f"Your cards are: {userCards} and your score is: {userScore}")
                    print(f"Computer's final hand is: {computerCards} and it's score was: {computerScore}")
                    print("YOU LOSE!, Your score is above 21.")
                    break
            else:
                print(f"Your cards are: {userCards} and your score is: {userScore}")
                print(f"Comptuter's first card: {computerCards[0]}")

        elif userChose == "n":
            cardGiving = False
            while computerScore < 17:
                computerCards.append(cardChoose())
                computerScore = sum(computerCards)
            print(f"Your final hand is: {userCards} and your score is: {userScore}")
            print(f"Computer's final hand is: {computerCards} and it's final score is: {computerScore}")
            
            if (computerScore > 21):
                print("YOU WIN!, Computer hand is above 21!")
            elif (userScore > computerScore):
                if 10 in userCards and 11 in userCards:
                    print("YOU WIN!, Your hand was BlackJack!")
                else:
                    print("YOU WIN!, Your hand is greater than the computer.")
            elif computerScore > userScore:
                if 10 in computerCards and 11 in computerCards:
                    print("YOU LOSE!, Computer hand was BlackJack!")
                else:
                    print("YOU LOSE!, Computer hand is greater than yours.")
            elif computerScore == userScore:
                if (10 in computerCards) and (11 in computerCards) and (10 in userCards) and (11 in userCards):
                    print("IT IS A DRAW! But with a two hand of BlackJack!!!")
                else:
                    print("IT IS A DRAW!")
