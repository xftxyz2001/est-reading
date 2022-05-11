with open('HDFPATP.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    with open('HDFPATP译文.md', 'w', encoding='utf-8') as fout:
        for line in lines:
            try:
                if line == '\n':
                    fout.write('\n')
                    continue
                elif line.startswith('#'):
                    fout.write(line)
                    continue
                startindex = line.index('（')
                endindex = line.index('）')
                fout.write(line[startindex+1:endindex] + '\n')
            except:
                continue
