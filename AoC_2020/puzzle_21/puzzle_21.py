from pathlib import Path
from parse import parse
from collections import defaultdict

filename = "input_21.txt"
food = defaultdict(list)
lines = []
with Path(filename).open() as file:
    for line in file:
        p = parse('{ingredients} (contains {allergens})', line)
        allergens = p['allergens'].split(", ")
        ingredients = set(p['ingredients'].split())
        lines.append(p['ingredients'].split())
        for a in allergens:
            food[a].append(ingredients)

common_ingredients = {}
for allergen in food:
    common_ingredients[allergen] = set.intersection(*food[allergen])

while True:
    if all([len(x) == 1 for x in common_ingredients.values()]):
        break
    for allergen in common_ingredients:
        if len(common_ingredients[allergen]) == 1:
            ingred = next(iter(common_ingredients[allergen]))
            for a in common_ingredients:
                if a != allergen:
                    common_ingredients[a].discard(ingred)

print(common_ingredients)
ing = []
for al in sorted(list(common_ingredients.keys())):
    ing.append(common_ingredients[al].pop())
print(','.join(ing))

problems = []
for allergen, value in common_ingredients.items():
    problems.append(value.pop())

total = 0
for l in lines:
    total += len([x for x in l if x not in problems])

print(total)
