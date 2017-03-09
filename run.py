import sys
from pdf_to_text import TextParser
from word_values import WordValues


if __name__ == '__main__':
    parser = TextParser(sys.argv[1])
    text = parser.output_text
    word_values = WordValues.word_values
