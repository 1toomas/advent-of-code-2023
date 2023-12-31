# https://adventofcode.com/2023/day/7
# Day 7: Camel Cards

filename = "inputs/day7-input.txt"
# filename = "inputs/day7-input-test.txt"

card_ranks = {"A":13, "K":12, "Q":11, "J":10, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
type_ranks = {"Five of a kind":7, "Four of a kind":6, "Full house":5, "Three of a kind":4, "Two pair":3, "One pair":2, "High card":1}

# determine the type of the hand, the rank of the type, and its strength based on card ranks
def hand_type(hand):
  cards_in_hand = dict() # find how many of each card are there in the hand
  # the strength of a hand based on card is the sequence of their individual rankings in the appearing order
  cards_strengths = ""
  for c in hand:
    cards_strengths += str(card_ranks[c]).zfill(2)
    if cards_in_hand.get(c) == None:
      cards_in_hand[c] = 1
    else:
      cards_in_hand[c] += 1
  # find the type of the hand
  if 5 in cards_in_hand.values(): # all five cards have the same label
    h_type = "Five of a kind"
  elif 4 in cards_in_hand.values(): # four cards have the same label
    h_type =  "Four of a kind"
  elif 3 in cards_in_hand.values() and 2 in cards_in_hand.values():
    # three cards have the same label, and the remaining two cards share a different label
    h_type =  "Full house"
  elif 3 in cards_in_hand.values():
    # three cards have the same label, and the remaining two cards are each different from any other card in the hand
    # the latter is assumed from the previous elif
    h_type =  "Three of a kind"
  elif len(cards_in_hand.values()) == 3:
    # two cards share one label, two other cards share a second label, and the remaining card has a third label
    # the amount of different cards as the only option us assumed from the previous elifs
    h_type =  "Two pair"
  elif len(cards_in_hand.values()) == 4:
    # two cards share one label, and the other three cards have a different label from the pair and each other
    h_type =  "One pair"
  elif len(cards_in_hand.values()) == 5: # all cards' labels are distinct
    h_type =  "High card"
  # ranking is the overall strength of the hand taking into account both the type and cards of the hand
  ranking = str(type_ranks[h_type]) + cards_strengths
  return (ranking, h_type, type_ranks[h_type], cards_strengths)

###
with open(filename, "r") as f:
  lines = f.readlines()

# store for each hand: [hand, winning, (ranking, type of hand, rank of hand's type, strength of hand's cards)]
hands = []
for l in lines:
  hands.append((l.split()[0], int(l.split()[1]), hand_type(l.split()[0])))

mysort = lambda a : a[2][0] # sorting function simply takes the ranking
# sort the hands by their rankings (i.e. first by hand type and then by strength of the cards of the hand)
hands.sort(key = mysort)

# total winning is sum of the winnings of each hand multiplied by the rank of the hand in the set
total_winnings = 0
for i in range(len(hands)):
  # rank starts from 1 and is multiplied by the winning of the hand
  total_winnings += (i+1) * hands[i][1]

print("The total winnings are "+str(total_winnings))
