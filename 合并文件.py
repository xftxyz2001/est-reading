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
    merge = MergeFiles('Summary-HDFPATP.md',
                       'Vocabulary analysis-HDFPATP.md')
    merge.merge_files('merged.md')
