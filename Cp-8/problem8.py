def rem(l, word):
    n = []

    for item in l:
        if item != word:
            n.append(item)

    return n


l = ["niloy", "prema", "aritra", "anika"]

print(rem(l, "anika"))