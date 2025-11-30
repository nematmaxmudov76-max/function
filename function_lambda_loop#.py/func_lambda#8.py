def func():
    katta = lambda s: s.upper()
    kichik = lambda s: s.lower()
    sarlavha = lambda s: s.title()
    return katta, kichik, sarlavha

# Ularni ro‘yxatda saqlaymiz


# Sinov uchun satr
matn = "python dasturlash tili"

# Har bir lambda funksiyani qo‘llaymiz
for amal in func():
    print(amal(matn))