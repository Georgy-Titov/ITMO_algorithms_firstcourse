def Rabin_Carp(text, sub_text):
    c = 0
    sub_text_hash = hash(sub_text)
    sub_text_len = len(sub_text)
    for i in range(len(text) - sub_text_len + 1):
        if hash(text[i: i + sub_text_len]) == sub_text_hash:
            if text[i: i + sub_text_len] == sub_text:
                c += 1
                print(sub_text)

    return c


ref = open('Корпоративные ценности.txt', encoding='utf-8').read().split()
wiki = open('wiki.txt', encoding='utf-8').read().split()
plag, total = 0, 0

for i in range(len(ref) - 3):
    pat = " ".join(ref[i:i + 3])
    plag += Rabin_Carp(" ".join(wiki), pat)

for i in ref:
    total += len(i)

print(f'В тексте {round(plag / total * 100)} % плагиата')
