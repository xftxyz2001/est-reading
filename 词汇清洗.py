f = open('HDFPATP词汇表.md', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
words_set = set()
for line in lines:
    # if line.endswith('.\n'):
    # if line.endswith(',\n'):
    if len(line) <= 5:
        continue
        # line = line[:-2] + '\n'
    words_set.add(line)

words = list(words_set)
words.sort()

f = open('HDFPATP词汇表.md', 'w', encoding='utf-8')
f.write(''.join(words))
f.close()
