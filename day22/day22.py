from collections import deque


def parse(file):

    f = open(file)

    player1, player2 = f.read().split('\n\n')

    deck1 = deque()
    deck2 = deque()

    for l in player1.split('\n'):
        if l.startswith('Player'):
            continue
        deck1.append(int(l))

    for l in player2.split('\n'):
        if l.startswith('Player'):
            continue
        deck2.append(int(l))

    return (deck1, deck2)


def part1():
    (deck1, deck2) = parse('day22/input.txt')

    total_cards = len(deck1) + len(deck2)

    round = 1

    while len(deck1) != 0 and len(deck1) != total_cards:

        top1 = deck1.popleft()
        top2 = deck2.popleft()

        if top1 > top2:
            deck1.append(top1)
            deck1.append(top2)
        else:
            deck2.append(top2)
            deck2.append(top1)

        round += 1

    winning = None
    if len(deck1) == 0:
        winning = deck2
    else:
        winning = deck1

    score = 0
    for i, c in enumerate(reversed(winning)):
        score += (i + 1) * c

    print('part1: ', score)


def game(g, deck1, deck2, prev1, prev2):

    total_cards = len(deck1) + len(deck2)

    round = 1

    while len(deck1) != 0 and len(deck1) != total_cards:

        res = None

        deck1 = deque(deck1)
        deck2 = deque(deck2)

        if tuple(deck1) in prev1 or tuple(deck2) in prev2:
            return (1, None)

        prev1.add(tuple(deck1))
        prev2.add(tuple(deck2))

        top1 = deck1.popleft()
        top2 = deck2.popleft()

        if top1 <= len(deck1) and top2 <= len(deck2):
            (res, _) = game(g + 1, list(deck1)[0:top1], list(
                deck2)[0:top2], set(), set())

        else:
            if top1 > top2:
                res = 1
            else:
                res = 2

        if res == 1:
            deck1.append(top1)
            deck1.append(top2)
        else:
            deck2.append(top2)
            deck2.append(top1)

        round += 1

    winning = None
    if len(deck1) == 0:
        winning = deck2
    else:
        winning = deck1
    score = 0
    for i, c in enumerate(reversed(winning)):
        score += (i + 1) * c

    if len(deck1) == 0:
        return (2, score)
    else:
        return (1, score)


def part2():
    (deck1, deck2) = parse('day22/input.txt')
    (_, score) = game(1, deck1, deck2, set(), set())
    print('part 2:', score)


part1()
part2()
