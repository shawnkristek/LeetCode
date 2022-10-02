class Brute:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        while hand:
            # find current hand minimum
            hand_minimum = min(hand)
            # remove card from hand...
            hand.remove(hand_minimum)
            for i in range(1,groupSize):
                if (hand_minimum + i) in hand:
                    hand.remove(hand_minimum + i)
                else:
                    return False
        return True

class Greedy:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        # count the different cards
        counts = {}
        for card in hand:
            counts[card] = 1 + counts.get(card, 0)

        # sorted hand without duplicates
        mins = list(counts.keys())
        mins.sort()

        while mins:
            for next_card in range(mins[0], mins[0]+groupSize):
                next_card_count = counts.get(next_card, 0)
                # if consecutive card missing, result = False
                if next_card_count == 0:
                    return False
                # if last of this card, it should be the minimum in mins, result = False if not
                elif next_card_count == 1:
                    if mins[0] == next_card:
                        mins.pop(0)
                    else:
                        return False

                # decrement count
                counts[next_card] -= 1

        return True

# test
tests = [ 
    ([1,2,3,6,2,3,4,7,8],   3,  True),
    ([1,2,3,4,5],           4,  False),
]

for hand,groupSize,solution in tests:
    sol = Greedy()
    sol = sol.isNStraightHand(hand,groupSize)
    print( sol == solution )
