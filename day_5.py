#black jack game
from random import randint

card_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def count_points(hand):
    points = 0
    for value in hand:
        points += value
    return points

def add_card(points, choice):
    if choice == 'Y' or choice == 'y':
        points += randint(1,13)
    return points

def get_hand(size):
    hand = []
    for card in range(size):
        hand.append(randint(1,13))
        #hand = hand.append(int(randint(1,13)))
    return hand

"""a = (get_hand(4))
print(get_hand(4))
print(count_points(a))"""

def count_game():
    a = get_hand(2)
    p = count_points(a)
    print(f"Your current point is {p}")
    a = input("Do you want more cards?")
    while a == "yes" or a== 'y':
        p = add_card(p, a)
        print(f"Your current pts is {p}")
        if p >21:
            break
        a = input("Do you want more cards?")

    return print(p)

count_game()