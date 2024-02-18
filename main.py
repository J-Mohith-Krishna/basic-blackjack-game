import random

def deal_card():
    return random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

def calculate_score(cards):
    score = 0
    num_aces = cards.count('A')

    for card in cards:
        if card.isdigit():
            score += int(card)
        elif card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            if num_aces == 1:
                score += 11
            else:
                score += 1
        else:
            print("Invalid card:", card)

    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1

    return score

def main():
    print("Welcome to Blackjack!")

    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    while player_score < 21:
        if input("Do you want to draw another card? (yes/no): ").lower() == 'yes':
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
        else:
            break

    while dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final score: {player_score}")
    print(f"Dealer's final score: {
