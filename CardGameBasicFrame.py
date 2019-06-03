import random

suits = ['spades', 'diamonds', 'clubs', 'hearts']
CardsAceTop = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
CardsAceBot = ['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


def init_cards():
    cards = []
    for x in range(4):
        for y in range(0, 13):

            cards.append((suits[x], y))

    return cards


def give_cards(player_amount, card_count):
    extra_cards = []
    cards = init_cards()
    player_list = []
    if player_amount*card_count <= len(cards)+1:
        for n in range(player_amount):
            player_list.append([])
        for n in range(card_count*player_amount):
            chosen = random.choice(cards)
            player_list[n % player_amount].append(chosen)
            cards.remove(chosen)
        extra_cards = cards
    else:
        print('not enough cards to distribute')
    return player_list
