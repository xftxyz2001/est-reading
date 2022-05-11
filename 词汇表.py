import re
f = open('HDFPATP原文.md', 'r', encoding='utf-8')
content = f.read()
f.close()

# 按空格分词
words = content.split()

# 去重
words_set = set()
for word in words:
    if not bool(re.search('[a-zA-Z]', word)):
        continue  # 不含字母的词汇不加入
    if word.startswith('“') or word.startswith('('):
        continue  # 引号开头的词汇不加入
    if len(word) <= 2:
        continue  # 长度小于2的词汇不加入
    words_set.add(word)

# 排序
words = list(words_set)
words.sort()

with open('HDFPATP词汇表.md', 'w', encoding='utf-8') as f:
    for word in words:
        f.write(word + '\n')
