import ast
import random

##########
## DATA ##
##########

# import data for deck of flashcards from a text file
with open('DECK - template.txt', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.strip().replace('\n', ', ')
deck = list(ast.literal_eval(text))
# the deck of flashcards is a list of tuples, where each tuple is a flashcard
# the first element of each tuple is the "question" on the flashcard, and the second element of each is the "answer"

###############
## FUNCTIONS ##
###############

# shuffle the deck of flashcards
def shuffle_deck():
    global deck
    shuffled = random.sample(deck, len(deck))
    deck = shuffled
    return deck

# draw a card from the deck and display the question
def draw_card():
    global deck
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

# main loop to draw cards and show answers until the deck is empty or 'qq' and ENTHER are pressed
def main():
    shuffle_deck()
    card = None
    while True:
        if not card:
            response = input("Press ENTER to draw a card or 'qq' and ENTER to quit")
            if response == 'qq':
                print("Until next time!")
                break
            card = draw_card()
        else:
            input("Press ENTER to see the answer")
            show_answer(card)
            card = None

if __name__ == "__main__":
    main()
