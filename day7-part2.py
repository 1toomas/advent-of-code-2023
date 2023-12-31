# https://adventofcode.com/2023/day/7#part2
# Day 7: Camel Cards

filename = "inputs/day7-input.txt"
# filename = "inputs/day7-input-test.txt"

card_ranks = {"A":13, "K":12, "Q":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2, "J":1}
type_ranks = {"Five of a kind":7, "Four of a kind":6, "Full house":5, "Three of a kind":4, "Two pair":3, "One pair":2, "High card":1}

def hand_value(hand):
  # the strength of a hand based on card is the sequence of their individual rankings in the appearing order
  cards_strengths = ""
  for c in hand:
    cards_strengths += str(card_ranks[c]).zfill(2)
  return cards_strengths

def hand_type(hand_cards):
  # find the type of the hand
  if 5 in hand_cards: # all five cards have the same label
    h_type = "Five of a kind"
  elif 4 in hand_cards: # four cards have the same label
    h_type =  "Four of a kind"
  elif 3 in hand_cards and 2 in hand_cards:
    # three cards have the same label, and the remaining two cards share a different label
    h_type =  "Full house"
  elif 3 in hand_cards:
    # three cards have the same label, and the remaining two cards are each different from any other card in the hand
    # the latter is assumed from the previous elif
    h_type =  "Three of a kind"
  elif len(hand_cards) == 3:
    # two cards share one label, two other cards share a second label, and the remaining card has a third label
    # the amount of different cards as the only option us assumed from the previous elifs
    h_type =  "Two pair"
  elif len(hand_cards) == 4:
    # two cards share one label, and the other three cards have a different label from the pair and each other
    h_type =  "One pair"
  elif len(hand_cards) == 5: # all cards' labels are distinct
    h_type =  "High card"
  return h_type

def count_cards_in_hand(hand):
  cards = dict() # find how many of each card are there in the hand
  for c in hand:
    if cards.get(c) == None:
      cards[c] = 1
    else:
      cards[c] += 1
  return cards

# determine the type of the hand, the rank of the type, and its strength based on card ranks
def hand_info(hand):
  cards_in_hand = count_cards_in_hand(hand) # find how many of each card are there in the hand

  if "J" in hand:  # if the hand contains joker(s)...
    if cards_in_hand["J"] == 5: # special case where there are only jokers
      replaced_joker_hand = "AAAAA"
      cards_in_hand = count_cards_in_hand(replaced_joker_hand)
      type_of_hand = hand_type(cards_in_hand.values())
      max_type_of_hand = type_of_hand
      max_strength = str(type_ranks[type_of_hand]) + hand_value(hand)
      max_hand = replaced_joker_hand
    else:
      # find out what should be replaced by joker(s)
      max_type_rank = 0
      max_strength = ""
      max_hand = ""
      max_type_of_hand = ""
      # brute force
      for c in cards_in_hand:
        if c == "J":
          continue
        replaced_joker_hand = hand.replace("J",c)
        cards_in_hand = count_cards_in_hand(replaced_joker_hand)
        type_of_hand = hand_type(cards_in_hand.values())
        strength = str(type_ranks[type_of_hand]) + hand_value(hand)
        if strength > max_strength:
          max_strength = strength
          max_substitute = c
          max_hand = replaced_joker_hand
          max_type_of_hand = type_of_hand
  else:
    type_of_hand = hand_type(cards_in_hand.values())
    max_type_of_hand = type_of_hand
    strength = hand_value(hand)
    max_strength = str(type_ranks[type_of_hand]) + strength
    max_hand = hand

  return (max_strength, type_of_hand, max_hand, max_type_of_hand)

###
with open(filename, "r") as f:
  lines = f.readlines()

# store for each hand: [hand, winning, (ranking, type of hand, rank of hand's type, strength of hand's cards)]
hands = []
for l in lines:
  hands.append((l.split()[0], int(l.split()[1]), hand_info(l.split()[0])))

mysort = lambda a : a[2][0] # sorting function simply takes the ranking
# sort the hands by their rankings (i.e. first by hand type and then by strength of the cards of the hand)
hands.sort(key = mysort)

for h in hands:
  print(h)

# total winning is sum of the winnings of each hand multiplied by the rank of the hand in the set
total_winnings = 0
for i in range(len(hands)):
  # rank starts from 1 and is multiplied by the winning of the hand
  total_winnings += (i+1) * hands[i][1]

print("The total winnings are "+str(total_winnings))
