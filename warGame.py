import pygame as Pg
import CardGameBasicFrame as Cg

players = Cg.give_cards(2, 26)
print('Welcome to the card game War')
Pg.init()
surface=Pg.display.set_mode((100,100))

def main():
    def check_cards(index):
        p1 = players[0][index][1]
        p2 = players[1][index][1]
        print("player 1's draw:", Cg.CardsAceTop[p1], "|| player 2's draw:", Cg.CardsAceTop[p2], '\n')
        if p1 > p2:
            temp = players[1][slice(0, index + 1, 1)]
            players[0].extend(temp)
            for i in range(index + 1):
                players[1].pop(0)
            print('Player 1 wins that draw\n')
        elif p1 == p2:
            print('WAR')
            if len(players[0]) > 4 and len(players[1]) > 4:
                check_cards(index + 4)
            else:
                t = []
                if len(players[0]) > len(players[1]):
                    for i in range(index + 1):
                        t = players[1].pop(0)
                    players[0].append(t)
                else:
                    for i in range(index + 1):
                        t = players[1].pop(0)
                    players[0].append(t)

        else:
            temp = players[0][slice(0, index + 1, 1)]
            players[1].extend(temp)
            for i in range(index + 1):
                players[0].pop(0)
            print('Player 2 wins that draw\n')


    win = False
    while not win:
        input('Press enter to draw:\n')
        if len(players[0]) < 52 and len(players[1]) < 52:
            check_cards(0)
            print('card amounts:\nplayer 1:', len(players[0]), '|| player 2:', len(players[1]), '\n')

        else:
            win = True

    if len(players[0]) > len(players[1]):
        print('\nplayer 1 wins!!!')
    else:
        print('\nplayer 2 wins!!!')


main()