STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]

class FileReader:
    def __init__(self, filename):
        self.filename = filename.open()

    def read_contents(self):
        contents = self.filename.read()
        return contents

class WordList:
    def __init__(self, text):
        self.text = text
        self.words =[]

    def extract_words(self):
        import string
        self.words = self.text.lower().split()
        self.words = [word.strip(string.punctuation) for word in self.words]

    def remove_stop_words(self):
        self.words = [
            word 
            for word in self.words
            if not word in STOP_WORDS]

    def get_freqs(self):
        freqs = {
            word: self.words.count(word)
            for word in self.words
        }
        alpha_freqs = dict(sorted(freqs.items()))
        return dict(sorted(alpha_freqs.items(), key=lambda seq: seq[1], reverse=True))

class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        top_ten = []
        top_ten_words = []
        i = 0
        for item in self.freqs.items():
            if i < 10:
                top_ten.append(item)
                top_ten_words.append(item[0])
                i += 1
        longest_word = max(top_ten_words, key=len)
        for item in top_ten:
            print(f"{item[0].rjust(len(longest_word) + 2)} | {str(item[1]).ljust(3)}{item[1] * '*'}")

if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
