class MergeRows:
    def __init__(self, filename, encoding='utf-8'):
        self.filename = filename
        self.file = open(filename, 'r', encoding=encoding)
        self.lines = self.file.readlines()
        self.file.close()

    def merge(self, outfilename, encoding='utf-8'):
        with open(outfilename, 'w', encoding=encoding) as outfile:
            for line in self.lines:
                if line == '\n':
                    outfile.write('\n\n')
                else:
                    outfile.write(line)
