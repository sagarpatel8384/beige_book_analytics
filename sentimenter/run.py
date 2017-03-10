import sys
import pprint
from pdf_to_text import TextParser
from analyze_text import AnalyzeText



if __name__ == '__main__':
    parser = TextParser(sys.argv[1])
    text = parser.output_text
    analyzed_text = AnalyzeText(text)
    print("Total Sentiment Score: {0}".format(analyzed_text.total_score))
    print("Average Sentiment Score: {0}".format(analyzed_text.avg_score))
    pprint.pprint(analyzed_text.histogram)

