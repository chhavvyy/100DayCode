''' Our Blackjack Game House Rules , The deck is unlimited in size. There are no jokers. The Jack/Queen/King all count as 10. The Ace can count as 11 or 1.
Use the following list as the deck of cards: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn. Cards are not removed from the deck as they are drawn. The computer is the dealer.'''

#--------------------------------------------------------------------------------------------------------------------------------------


import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,]
crazy = True
haha = True
while crazy:
    x = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
    if x=='y':
        haha = True
        while haha:

                        hah = []
                        heh = []
                        print("hi")

                        y=random.choice(cards)
                        y2=random.choice(cards)
                        hah.extend([y,y2])
                        total= y + y2

                        z = random.choice(cards)
                        heh.append(z)
                        total_comp = z

                        print(f"Your cards : {hah}; current score: {total} \n Computer's first card: {z}")
                        x2=input("Type 'y' to get another card, type 'n' to passsss:")

                        if x2=='y':
                                    y3=random.choice(cards)
                                    hah.append(y3)
                                    total2 = y + y2 + y3
                                    print(f"Your cards:\t{hah}; current score: {total2} \n Computer's first card: {[z]}\n Computer's final hand ; {heh}, final score:{total_comp}")
                                    if total2>total_comp:
                                        if total2<=21:
                                            print("you win wow")
                                            crazy = True
                                            haha = False
                                        else:
                                            print("you went over. you lose")
                                            crazy = True
                                            haha = False
                                    elif total2==total_comp:
                                        print("draw hurray")
                                        crazy = True
                                        haha = False
                                    else:
                                        if total_comp<=21:
                                            print("you lose aww")
                                            crazy = True
                                            haha = False
                        elif x2 == 'n':
                            z2=random.choice(cards)
                            z3= random.choice(cards)
                            heh.extend([z2,z3])
                            total_comp2 = z + z2 + z3
                            print(f"computer's cards:\t{heh}; current score: {total_comp2} \n Computer's final hand ; {heh}, final score:{total_comp2}")
                            print(total_comp2)
                            if total_comp2 > total :
                                if total_comp2<=21:
                                    print("dealer's win")
                                    crazy = True
                                    haha = False
                                else:
                                    print("dealer went over. you win")
                                    crazy = True
                                    haha = False
                            elif total_comp2==total:
                                print("draw haha")
                                crazy = True
                                haha = False
                            else:
                                    if total<=21:
                                        print("you win yeya")
                                        crazy = True
                                        haha = False
                                    else:
                                        break
                        else:
                           print("nopes")
                           haha = False
                           crazy = True
    elif x == 'n':
        print("exited")
        break


    else:
        print("exited")
