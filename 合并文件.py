class MergeFiles:
    def __init__(self, *args):
        self.files = args

    def merge_files(self, outfilename, encoding='utf-8', sep='\n'):
        with open(outfilename, 'w', encoding=encoding) as fout:
            for filename in self.files:
                with open(filename, 'r', encoding=encoding) as fin:
                    fout.write(fin.read())
                    fout.write(sep)


if __name__ == '__main__':
    merge = MergeFiles('Summary-Healthy Diets for People and the Planet.md',
                       'Vocabulary analysis-Healthy Diets for People and the Planet.md')
    merge.merge_files('merged.md')
