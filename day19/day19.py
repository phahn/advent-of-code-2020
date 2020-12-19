import re

def solve(part2):

    f = open('day19/input.txt')
    (rules, messages) = f.read().split('\n\n')

    RULES = {}
    for r in rules.split('\n'):
        (idx, rule) = r.split(':')
        RULES[idx] = rule.strip()

    R0 = RULES['0']

    regex = []

    # number of times to expand regex
    NUM_EXPANSIONS = 10

    def substitute(R, regex):
        if part2 and R.strip() == '42':
            regex.append("(")
            substitute(RULES['42'], regex)
            regex.append(")+")
            return

        if part2 and R.strip() == '42 31':
            regex.append("(")
            # expanding rules
            for i in range(1, NUM_EXPANSIONS):
                for _ in range(i):
                    substitute(RULES['42'], regex)
                for _ in range(i):
                    substitute(RULES['31'], regex)
                if i < NUM_EXPANSIONS - 1:
                    regex.append("|")

            regex.append(")")
            return

        subs = R.split("|")

        if len(subs) == 1:
            tokens = R.split(" ")
            for c in tokens:
                if c.isdecimal():
                    substitute(RULES[c], regex)
                elif c.startswith("\""):
                    regex.append(c[1])
        elif len(subs) == 2:
            regex.append("(")
            substitute(subs[0], regex)
            regex.append('|')
            substitute(subs[1], regex)
            regex.append(")")
        else:
            raise 'ERROR'

    regex.append("^")
    substitute(R0, regex)
    regex.append('$')
    pattern = "".join(regex)

    sum = 0
    for m in messages.split('\n'):
        if re.match(pattern, m):
            sum += 1
    print(sum)


solve(False)
solve(True)
