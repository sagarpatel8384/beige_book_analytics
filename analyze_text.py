from word_values import WordValues

class AnalyzeText:
    """
    The AnalyzeText class compares words in a string to the values assigned
    to those words and computes a overall score
    """

    def __init__(self, text):
        analyzed_text = self.analyze_text(text)
        keyword_scores = analyzed_text[0]
        keyword_count = analyzed_text[1]

        self.total_score, self.avg_score = self.compute_scores(keyword_scores)
        self.histogram = self.compute_histogram(keyword_count)

    def analyze_text(self, text):
        keyword_values = {}
        keyword_count = {}
        normalized_text_tuple = text.lower().split(" ")

        for word in normalized_text_tuple:
            if word in WordValues.keyword_values:
                keyword_count[word] = 1 if keyword_count.get(word) == None else keyword_count[word] + 1
                keyword_values[word] = WordValues.keyword_values[word] if keyword_values.get(word) == None else keyword_values[word] + WordValues.keyword_values[word]

        return (keyword_values, keyword_count)

    def compute_scores(self, keyword_scores):
        keyword_scores_list = tuple(keyword_scores.values())
        total_score = sum(keyword_scores_list)
        avg_score = total_score / len(keyword_scores_list)

        return (total_score, avg_score)

    def compute_histogram(self, keyword_count):
        return { word: "#" * count for word, count in keyword_count.items() }
