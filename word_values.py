class WordValues:
    """
    The Word Values Class is a namespace for the word/value pairs.
    This class is not intended to be instantiated; rather, its purpose
    is to act as a namespace to access the word_values dictionary without
    polluting the global scope.
    """

    keyword_values = {
        'strong': 1,
        'robust': 1,
        'considerable': 1,
        'upbeat': 1,
        'brisk': 1,
        'surge': 1,
        'normal': 0.75,
        'solid': 0.75,
        'steady': 0.75,
        'modest': 0.50,
        'moderate': 0.50,
        'sustainable': 0.50,
        'slow': 0.25,
        'gradual': 0.25,
        'subdued': 0.25,
        'muted': 0.25,
        'unclear': 0,
        'mixed': 0,
        'decelerating': -0.20,
        'stabilizing': -0.20,
        'ongoing adjustment': -0.20,
        'leveling out': -0.20,
        'continued weakness': -0.50,
        'sluggish': -0.50,
        'slack': -0.50,
        'below potential': -0.50,
        'declining': -0.75,
        'deteriorating': -0.75,
        'recession': -1,
        'contraction': -1,
        'sharp and widespread decline': -1
    }
