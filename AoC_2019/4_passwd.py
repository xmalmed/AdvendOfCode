seznam = []

r1 = 277777
# r2 = 277888
r2 = 799999

def test_int(cislo):
    if (100000 * int(cislo[0]) + 10000 * int(cislo[1]) + 1000 * int(cislo[2]) + 100 * int(
            cislo[3]) + 10 * int(cislo[4]) + int(cislo[5]) >= r1) \
            and \
            (100000 * int(cislo[0]) + 10000 * int(cislo[1]) + 1000 * int(cislo[2]) + 100 * int(
                cislo[3]) + 10 * int(cislo[4]) + int(cislo[5]) <= r2):
        return True


for i in range(r1, r2 + 1):
    cislo = sorted(str(i))
    # spatna delka
    if len(set(cislo)) == 5:
        if test_int(cislo):
            seznam.append(tuple(cislo))
    elif len(set(cislo)) == 1:
        pass
    elif len(set(cislo)) < 5:
        if test_int(cislo):
            k = 1
            t = False
            for j in range(5):
                if cislo[j] == cislo[j + 1]:
                    k += 1
                else:
                    if k == 2:
                        t = True
                    k = 1
            if t or (k == 2):
                seznam.append(tuple(cislo))

print(set(seznam))
print(len(set(seznam)))
