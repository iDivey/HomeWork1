def all_variants(txt):
    t = len(txt)
    for i in range(t):
        for o in range(t - i):
            yield txt[o:o + 1 + i]


a = all_variants("abc")
for e in a:
    print(e)
