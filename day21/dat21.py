from collections import defaultdict


def parse_rules():
    f = open('day21/input.txt')
    ALL_INGREDIENTS = set()
    ALL_ALLERGENS = set()
    rules = []
    for line in f.readlines():
        ingredients = set()
        allergens = set()
        flist, ilist = line.split("(")
        for food in flist.strip().split(" "):
            ingredients.add(food)
            ALL_INGREDIENTS.add(food)
        for allergen in ilist.strip()[:-1].split(" "):
            if allergen == 'contains':
                continue
            if allergen[-1] == ",":
                allergen = allergen[:-1]
            allergens.add(allergen)
            ALL_ALLERGENS.add(allergen)
        rules.append((ingredients, allergens))
    return rules


def get_all_ingredients(rules):

    ing = set()
    for rule in rules:
        (ingredients, _) = rule
        for i in ingredients:
            ing.add(i)
    return ing


def get_all_allergens(rules):

    ing = set()
    for rule in rules:
        (_, allergens) = rule
        for i in allergens:
            ing.add(i)
    return ing


def get_impossible_allergens_for_ingredient(rules, ALL_INGREDIENTS):
    #  ingredient -> set of allergens that cannot be contained
    I = defaultdict(set)

    for rule in rules:
        ingredients, allergens = rule
        for a in allergens:
            for i in ALL_INGREDIENTS:
                if i not in ingredients:
                    I[i].add(a)
    return I


def get_unique_allergens_for_ingredient(rules, ALL_INGREDIENTS):
    U = {}
    for rule in rules:
        ingredients, allergens = rule
        if len(ingredients) == 1 and len(allergens) == 1:
            U[list(ingredients)[0]] = list(allergens)[0]
    return U


def get_possible_ingredients_for_allergens(rules, ALL_ALLERGENS):
    U = defaultdict(set)
    for rule in rules:
        ingredients, allergens = rule
        for a in allergens:
            for i in ingredients:
                U[a].add(i)
    return U


rules = parse_rules()

start_ingredients = get_all_ingredients(rules)

KNOWN = {}

step = 0
while len(KNOWN) < len(start_ingredients):

    ALL_INGREDIENTS = get_all_ingredients(rules)
    ALL_ALLERGENS = get_all_allergens(rules)

    I = get_impossible_allergens_for_ingredient(rules, ALL_INGREDIENTS)

    INGREDIENTS_WITHOUT_ALLERGENS = set()
    for i in I:
        if len(I[i]) == len(ALL_ALLERGENS):
            INGREDIENTS_WITHOUT_ALLERGENS.add(i)

    for i in INGREDIENTS_WITHOUT_ALLERGENS:
        KNOWN[i] = None

    U = get_unique_allergens_for_ingredient(rules, ALL_INGREDIENTS)

    for u in U:
        KNOWN[u] = U[u]

    V = get_possible_ingredients_for_allergens(rules, ALL_ALLERGENS)

    #  part 1
    if step == 0:
        count = 0
        for rule in rules:
            ingredients, _ = rule
            for i in ingredients:
                if i in INGREDIENTS_WITHOUT_ALLERGENS:
                    count += 1
        print('part 1:', count)

    CANDIDATES = defaultdict(set)
    for i in ALL_INGREDIENTS:
        for a in ALL_ALLERGENS:
            if i not in INGREDIENTS_WITHOUT_ALLERGENS and a not in I[i]:
                CANDIDATES[i].add(a)
        if len(CANDIDATES[i]) == 1:
            KNOWN[i] = list(CANDIDATES[i])[0]

    #  remove knowns from rules
    new_rules = []
    for rule in rules:
        ingredients, allergens = rule
        new_ingredients = set()
        new_allergens = set()
        for a in allergens:
            if a not in set(KNOWN.values()):
                new_allergens.add(a)
        for i in ingredients:
            if i not in KNOWN:
                new_ingredients.add(i)
        if len(new_allergens) > 0:
            new_rules.append((new_ingredients, new_allergens))
    rules = new_rules

    step += 1


inv_map = {v: k for k, v in KNOWN.items() if v is not None}
part2 = []
for k in sorted(inv_map):
    part2.append(inv_map[k])
print('part 2:', ",".join(part2))
