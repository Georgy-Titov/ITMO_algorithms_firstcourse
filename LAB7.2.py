def naive(s, pat):
    m = len(pat)
    c = 0
    for i in range(len(s) - m):
        if s[i:i + m] == pat:
            for j in pat:
                c += len(j)
    return c


ref = open('Корпоративные ценности.txt', encoding='utf-8').read().split()
wiki = open('wiki.txt', encoding='utf-8').read().split()
plag, total = 0, 0

for i in range(len(ref) - 3):
    pat = ref[i:i + 3]
    plag += naive(wiki, pat)

for i in ref:
    total += len(i)

print(f'В тексте {round(plag / total * 100)} % плагиата')
