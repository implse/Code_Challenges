# https://codefights.com/interview-practice/task/xrFgR63cw7Nch4vXo

# You have a list of dishes. Each dish is associated with a list of ingredients used to prepare it.
# You want to group the dishes by ingredients, so that for each ingredient you'll be able to find
# all the dishes that contain it (if there are at least 2 such dishes).

def groupingDishes(dishes):
    ingredients = dict()
    for d in dishes:
        for i in range(1, len(d)):
            if d[i] not in ingredients:
                ingredients[d[i]] = list()
            if d[0] not in ingredients[d[i]]:
                ingredients[d[i]].append(d[0])
    elements = list()
    for key, value in ingredients.items():
        r = list()
        r.append(key)
        if len(value) > 1:
            for v in sorted(value):
                r.append(v)
            elements.append(r)
    return sorted(elements)
