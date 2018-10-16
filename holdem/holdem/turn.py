from typing import List

from .core.cards import Card
from .player import Other

def zip_suit(total_cards):
    by_suit = [(i, sorted([c for c in total_cards if c.suit == i],
                               key=lambda c:c.rank))
                     for i in range(1, 5)]
    by_suit = sorted(by_suit, key=lambda x: len(x[1]), reverse=True)
    max_length = len(by_suit[0][1])

    return by_suit, max_length

def zip_rank(total_cards):
    by_rank = [(i, sorted([c for c in total_cards if c.rank == i],
                               key=lambda c:c.suit))
                     for i in range(2, 15)]
    by_rank = sorted(by_rank, key=lambda x: len(x[1]), reverse=True)
    max_length = len(by_rank[0][1])

    return by_rank, max_length


def get_straight_cards(cards):
    if len(cards) < 5:
        return []
    sorted_cards = sorted(cards, key=lambda x:x.rank)

    straights = []
    diff = 0
    temp = []
    for i in range(1, len(sorted_cards)):
        if i == 1:
            temp.append(cards[i-1])

        diff = cards[i].rank - cards[i-1].rank

        if diff == 1:
            temp.append(cards[i])
        elif diff != 1:
            straights.append(temp)
            temp = [cards[i]]

        if i == len(sorted_cards) - 1:
            straights.append(temp)

    return max(straights, key=lambda x:len(x))


def is_royal_flush(by_suit):
    if len(by_suit[0]) < 5:
        return False

    by_suit_straight = get_straight_cards(by_suit[0])
    if len(by_suit_straight) >= 5 \
            and by_suit_straight[-1].rank == 14:
        return True
    else:
        return False


def is_straight_flush(by_suit):
    if len(by_suit[0]) < 5:
        return False

    by_suit_straight = get_straight_cards(by_suit[0])
    if len(by_suit_straight) >= 5:
        return True
    else:
        return False


def is_four_card(by_rank):
    if len(by_rank[0]) >= 4:
        return True
    else:
        return False


def is_full_house(by_rank):
    if len(by_rank[0]) >= 3 \
            and len(by_rank[1]) >= 2:
        return True
    else:
        return False


def is_flush(by_suit):
    if len(by_suit[0]) >= 5:
        return True
    else:
        return False


def is_straight(total_cards):
    if len(get_straight_cards(total_cards)) >= 5:
        return True
    else:
        return False

def is_triple(by_rank):
    if len(by_rank[0]) >= 3:
        return True
    else:
        return False


def is_two_pair(by_rank):
    if len(by_rank[0]) >= 2 and len(by_rank[1]) >= 2:
        return True
    else:
        return False


def is_one_pair(by_rank):
    if len(by_rank[0]) >= 2:
        return True


def bet(
    my_chips: int, # 남은 칩 수
    my_cards: List[Card], # 플레이어의 손 패 (2장)
    bet_players: List[Other], # 이번 턴에 베팅한 플레이어들 
    betting_players: List[Other], # 아직 베팅하지 않은 플레이어들
    community_cards: List[Card], # 커뮤니티 카드 + 턴 카드 + 리버 카드 (3장 ~ 5장)
    min_bet_amt: int, # 가능한 최소 베팅액
    max_bet_amt: int, # 가능한 최대 베팅액
    total_bet_amt: int # 여태까지 베팅한 누적 금액
) -> int:

    # 플랍카드 안받았을 때
    if len(community_cards) == 0:
        if my_cards[0].rank == my_cards[1].rank \
                or my_cards[0].suit == my_cards[1].suit:
            return min(my_chips, max_bet_amt)
        else:
            return 0

    total_cards = sorted(my_cards + community_cards, key=lambda x: x.rank)

    by_suit, max_suit_length = zip_suit(total_cards)
    by_rank, max_rank_length = zip_rank(total_cards)

    # 플랍카드 1장 오픈후(총 5장 오픈, 마지막)
    if is_royal_flush(by_suit):
        # print('[1] 로열 플러쉬!!!!!')
        return max(min(my_chips, max_bet_amt), min_bet_amt)

    if is_straight_flush(by_suit):
        # print('[2] 스트레이트 플러쉬!!!!!')
        return max(min(my_chips, max_bet_amt), min_bet_amt)

    if is_four_card(by_rank):
        # print('[3] 포카드!!!!!')
        return max(min(my_chips, max_bet_amt), min_bet_amt)

    if is_full_house(by_rank):
        # print('[4] 풀하우스!!!!!')
        return max(min(my_chips, max_bet_amt), min_bet_amt)

    if is_flush(by_suit):
        return max(min(my_chips, max_bet_amt), min_bet_amt)

    if is_straight(total_cards):
        # print('[6] 스트레이트!!!!!')
        if len([other.bet_amt for other in bet_players if other.bet_amt >= int(other.chips/3)]) > 0:
            return min_bet_amt
        else:
            return max(min(my_chips, max_bet_amt), min_bet_amt)

    if is_triple(by_rank):
        if len([other.bet_amt for other in bet_players if other.bet_amt >= int(other.chips/3)]) > 0:
            return min_bet_amt
        else:
            return max(min(my_chips, max_bet_amt), min_bet_amt)

    if is_two_pair(by_rank):
        return min_bet_amt

    return 0
