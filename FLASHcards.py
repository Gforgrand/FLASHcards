import os
import ast
import random

# the deck of flashcards is a list of tuples, where each tuple is a flashcard
# the first element of each tuple is the "question" on the flashcard, and the second element of each is the "answer"

###############
## FUNCTIONS ##
###############

# import data for deck of flashcards from a text file
def select_data():
    files = [f for f in os.listdir() if f.endswith('.txt')]
    print("Select a file to open:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")
    choice = int(input("Enter the number of the file you want to open: "))
    filename =  files[choice-1]

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.strip().replace('\n', ', ')
    deck = list(ast.literal_eval(text))
    return deck

# shuffle the deck of flashcards
def shuffle_deck(deck):
    shuffled = random.sample(deck, len(deck))
    deck = shuffled
    return deck

# draw a card from the deck and display the question
def draw_card(deck):
    if len(deck) > 0:
        card = deck.pop(0)
        print(card[0])
        return card
    else:
        print("The deck is empty.")
        return None

# display the answer for the currently drawn card
def show_answer(card):
    if card:
        print(card[1])
    else:
        print("No card has been drawn.")

##########
## MAIN ##
##########

# main loop to draw cards and show answers until the deck is empty or 'qq' and ENTER are pressed
def main():
    deck = select_data()
    shuffle_deck(deck)
    card = None
    while True:
        if not card:
            response = input("Press ENTER to draw a card or 'qq' and ENTER to quit")
            if response == 'qq':
                break
            card = draw_card(deck)
        else:
            input("Press ENTER to see the answer")
            show_answer(card)
            card = None

if __name__ == "__main__":
    main()
