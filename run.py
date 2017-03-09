import sys
from pdf_to_text import TextParser


if __name__ == '__main__':
    p = TextParser(sys.argv[1])
    output = open('output.txt', 'w')
    output.write(p.output_text)
    output.close()
