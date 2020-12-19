from collections import deque


def get_tokens(s):
    a = deque()
    i = 0
    n = len(s)
    while i < n:
        if s[i] in "+*()":
            a.append(s[i])
            i += 1
        elif s[i].isdigit():
            j = i
            while i < n and s[i].isdigit():
                i += 1
            a.append(s[j:i])
        elif s[i].isspace():
            i += 1
        else:
            raise SyntaxError()
    return a


def solve(s, prio):
    output = deque()
    operators = deque()
    tokens = get_tokens(s)

    # shunting yard algorithm to transform infix into reverse polnish notation
    while tokens:
        token = tokens.popleft()
        if token.isdecimal():
            output.append(token)
        if token == "*" or token == "+":
            while len(operators) > 0 and operators[len(operators) - 1] != "(" and not (prio[operators[len(operators) - 1]] < prio[token]):
                op = operators.pop()
                output.append(op)
            operators.append(token)
        if token == "(":
            operators.append(token)
        if token == ")":
            while len(operators) > 0 and operators[len(operators) - 1] != "(":
                op = operators.pop()
                output.append(op)
            if operators[len(operators) - 1] == "(":
                op = operators.pop()

    while operators:
        output.append(operators.pop())

    # evaluate reverse polish notation
    result = deque()

    while output:
        token = output.popleft()
        if token.isdecimal():
            result.append(int(token))
        if token == '+':
            op1 = result.pop()
            op2 = result.pop()
            result.append(op1 + op2)
        if token == '*':
            op1 = result.pop()
            op2 = result.pop()
            result.append(op1 * op2)

    return result[0]


def part1():

    prio = {"*": 0, "+": 0}

    assert solve('1 + 2 * 3 + 4 * 5 + 6', prio) == 71
    assert solve('1 + (2 * 3) + (4 * (5 + 6))', prio) == 51
    assert solve('2 * 3 + (4 * 5)', prio) == 26
    assert solve('5 + (8 * 3 + 9 + 3 * 4 * 3)', prio) == 437
    assert solve('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', prio) == 12240
    assert solve(
        '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', prio) == 13632

    sum = 0
    for line in open('day18/input.txt'):
        sum += solve(line.strip(), prio)
    print('part 1', sum)


part1()


def part2():

    prio = {"*": 0, "+": 1}

    assert solve('1 + 2 * 3 + 4 * 5 + 6', prio) == 231
    assert solve('1 + (2 * 3) + (4 * (5 + 6))', prio) == 51
    assert solve('2 * 3 + (4 * 5)', prio) == 46
    assert solve('5 + (8 * 3 + 9 + 3 * 4 * 3)', prio) == 1445
    assert solve('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', prio) == 669060
    assert solve(
        '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', prio) == 23340

    sum = 0
    for line in open('day18/input.txt'):
        sum += solve(line.strip(), prio)
    print('part 2', sum)


part2()
