from faker import Faker

class generator:

    def __init__(self):
        self.faker  = None
        self.current_text = None

        self.diff_level = None
        self.diff_settings = {
            'difficulty' : None ,
            'word_count' : None ,
            'punctuation' : None ,
            'technical_words' : None ,
            'long_terms' : None, 
            'capitalization' : None,
            'case_variation' : None,
            'random_caps' : None, 
        }

        self.min_words = None
        self.max_words = None

        self.easy_diff = None
        self.medium_diff = None
        self.hard_diff = None

    def difficulty(self):

        def easy():
            self.diff_settings['word_count'] = 150

        def medium():
            self.diff_settings['word_count'] = 150 
            self.diff_settings['capitalization'] = True
            self.diff_settings['case_variation'] = True

        def hard():
            self.diff_settings['word_count'] = 150 
            self.diff_settings['capitalization'] = True
            self.diff_settings['case_variation'] = True
            self.diff_settings['random_caps'] = True
            self.diff_settings['technical_words'] = True
            self.diff_settings['long_terms'] = True
        return {"easy": easy, "medium": medium, "hard": hard}