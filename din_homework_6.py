
#1. Mbox-short.txt faylini oching, ushbu fayldagi har bir satrni "o'qing" va unga mos keladigan qatorlarni toping:
# "From Stephen.marquard@uct.ac.za Sat 5 Jan 09:14:16 2008" . Keyin barcha INBOX elektron pochta manzillarini va umumiy sonni chop eting.
# Ushbu muammoni hal qilish uchun string usullaridan foydalaning.

#
# with open('mbox-short.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         if "From Stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008".lower() in line.lower():
#             print(line)

#
# with open('mbox-short.txt', mode = 'r') as file:
#     count = 0
#     for line in file:
#         line = line.strip()
#         if line.startswith('From'):
#             print(line.split()[1])
#             count += 1
#     print('Umumiy emaillar soni:', count)


# 2. Muayyan fayl faylini ochadigan read_last(chiziqlar, fayl) funksiyasini yozing va oxirgi satrlarni satrlar soni boʻyicha satr boʻyicha chop eting
# (har holda, berilgan butun son musbat son ekanligini tekshirib koʻraylik).
# Funksiyani quyidagi mazmun bilan “article.txt” faylida sinab ko‘raylik:

# def read_last(chiziqlar, file):
#     if chiziqlar <= 0 :
#         print('Iltimos, musbat son kiriting')
#         return
#     with open(file, mode = 'r', encoding = 'utf-8') as file:
#         satrlar = file.readlines()
#         last_lines = satrlar[-chiziqlar:]
#         for line in last_lines:
#             print(line.strip())
# read_last(3, 'article.txt')


# 3.Maksimal uzunlikdagi so'zni (yoki agar ular bir nechta bo'lsa, so'zlar ro'yxatini)
# aks ettiruvchi eng uzun_so'zlar(fayl) funksiyasini amalga oshirish talab etiladi.

# with open('article.txt', mode = 'r', encoding ='utf-8') as file:
#     all_words = []
#     for line in file:
#         words = line.split()
#         all_words.extend(words)
#
# max_length = max(len(word) for word in all_words)
# longest_words = [word for word in all_words if len(word) == max_length]
# print(longest_words)



# 4.romeo.txt faylini oching. Undagi har bir satrni "o'qing". Har bir satrdan alohida so'zlarni oling, so'ngra so'zlar ro'yxatini tuzing.
# Ro'yxatda so'zlar takrorlanmasligi kerak. Keyin barcha so'zlar alifbo tartibida tartiblangan ro'yxatni chop eting.

# with open('romeo.txt', mode = 'r') as file:
#     all_words = []
#     for line in file:
#         words = line.split()
#         all_words.extend(words)
#     unique_words = set(all_words)
#     sorted_words = sorted(unique_words)
#     print(sorted_words)


# 5.Pushkin.txt, byron.txt, romeo.txt fayllari tarkibini bitta Poems.txt fayliga birlashtiring.
# Har bir she'rning satrlarini kengaytiring. Masalan:



