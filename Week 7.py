

def ashar(n):
    before, after = round(2.3, 2), round((2.3 + 0.01), 2)
    for _ in range(n):
        if before == round(2.3, 2):
            yield before
        if after == round(3.79, 2):
            break
        else:
            yield after
            before, after = round(after, 2), round((after + 0.01), 2)


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def halfalphabet():
    per, cur = alphabet[2], alphabet[4]

    for _ in alphabet:
        if per == 'C':
            yield per
        if cur == 'Y':
            break
        else:
            yield cur
            per, cur = cur, alphabet[alphabet.index(cur)+2]


if __name__ == '__main__':

    asharSet = set()
    for number in ashar(1000):
        asharSet.add(number)
    print(asharSet)

    print('--------------------------------')

    for _ in halfalphabet():
        print(_)


