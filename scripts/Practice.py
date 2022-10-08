l = [5, 2, 5, 2, 2, 91]
uniques = list()
for item in l:
    if item not in uniques:
        uniques.append(item)

print(uniques)