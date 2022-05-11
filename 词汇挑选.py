f = open('HDFPATP词汇表.md', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
words_set = set()
for line in lines:
    if len(line) > 10:
        words_set.add(line.lower())

words = list(words_set)
words.sort()

f = open('HDFPATP长单词.md', 'w', encoding='utf-8')
f.write(''.join(words))
f.close()
