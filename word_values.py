class WordValues:
    """
    The Word Values Class is a namespace for the word/value pairs.
    This class is not intended to be instantiated; rather, its purpose
    is to act as a namespace to access the word_values dictionary without
    polluting the global scope.
    """

    word_values = {
        "strong": (1, ['strong', 'robust', 'considerable', 'upbeat', 'brisk', 'surge']),
        "normal": (0.75, ['normal', 'solid', 'steady']),
        "modest": (0.50, ['modest', 'moderate', 'sustainable']),
        "slow": (0.25, ['slow', 'gradual', 'subdued', 'muted']),
        "unclear": (0, ['unclear', 'mixed']),
        "decelerating": (-0.25, ['decelerating', 'stabilizing', 'ongoing adjustment', 'leveling out']),
        "continued_weakness": (-0.50, ['continued weakness', 'sluggish', 'slack', 'below potential']),
        "decline": (-0.75, ['declining', 'deteriorating']),
        "recession": (-1, ['recession', 'contraction', 'sharp and widespread decline'])
    }
