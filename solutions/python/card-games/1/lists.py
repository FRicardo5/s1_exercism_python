"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds = []
    for i in range(3):
        rounds.append(number)
        number+=1
    
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2
    


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    for i in rounds:
       if i == number:
           return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    qt_total = len(hand)
    vl_total = sum(hand)
    return vl_total/qt_total


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    
    last_card = hand[len(hand) - 1]
    first_card = hand[0]
    middle_card = hand[len(hand) // 2]
    
    average_hand = sum(hand) / len(hand)
    average_first_last_cards = (last_card + first_card) / 2
    
    if average_first_last_cards == average_hand:
        return True
    if middle_card == average_hand:
        return True
    return False
    

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    i = 0
    hand_even_index = []
    hand_odd_index = []
    for i in range(len(hand)): 
        if i % 2 == 0:
            hand_even_index.append(hand[i])
        else:
            hand_odd_index.append(hand[i])
    
    if (sum(hand_even_index) / len(hand_even_index)) == (sum(hand_odd_index) / len(hand_odd_index)):
        return True
    return False
    


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
