with open('Healthy Diets for People and the Planet.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    with open('Healthy Diets for People and the Planet原文.md', 'w', encoding='utf-8') as fout:
        for line in lines:
            if line.startswith('（'):
                continue
            fout.write(line)
