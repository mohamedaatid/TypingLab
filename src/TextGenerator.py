
import random
import sys
from faker import Faker

class Generator:

    def __init__(self):
        self.faker = Faker()
        self.current_text = None
        self.diff_settings = {
            'word_count': 150,
            'punctuation': False,
            'technical_words': False,
            'long_terms': False, 
            'capitalization': False,
            'case_variation': False,
            'random_caps': False, 
            'numbers': False,
        }

    def difficulty(self, level):

        def easy():
            self.diff_settings['word_count'] = 150
            # Reset all other settings to False for easy mode
            for key in self.diff_settings:
                if key != 'word_count':
                    self.diff_settings[key] = False

        def medium():
            self.diff_settings['word_count'] = 175 
            self.diff_settings['capitalization'] = True
            self.diff_settings['case_variation'] = True
            self.diff_settings['numbers'] = True
            # Reset unused settings
            self.diff_settings['random_caps'] = False
            self.diff_settings['technical_words'] = False
            self.diff_settings['long_terms'] = False
            self.diff_settings['punctuation'] = False

        def hard():
            self.diff_settings['word_count'] = 225
            self.diff_settings['capitalization'] = True
            self.diff_settings['case_variation'] = True
            self.diff_settings['random_caps'] = True
            self.diff_settings['technical_words'] = True
            self.diff_settings['long_terms'] = True
            self.diff_settings['numbers'] = True
            self.diff_settings['punctuation'] = False
            
        def custom():
            print("\n--- Configure Custom Difficulty ---")
            word_count = input("word_count: ").strip()
            self.diff_settings['word_count'] = int(word_count) if word_count.isdigit() else 150
            
            def get_bool(prompt):
                return input(f"{prompt} (y/n): ").lower().strip() in ['y', 'yes']

            self.diff_settings['capitalization'] = get_bool("Use sentence capitalization?")
            self.diff_settings['case_variation'] = get_bool("Randomly uppercase words?")
            self.diff_settings['random_caps'] = get_bool("Use random capitalization (LiKe tHiS)?")
            self.diff_settings['numbers'] = get_bool("Include random numbers?")
            self.diff_settings['technical_words'] = get_bool("Include technical words? (Placeholder)")
            self.diff_settings['long_terms'] = get_bool("Include long terms? (Placeholder)")

        if level == 'easy':
            easy()
        elif level == 'medium':
            medium()
        elif level == 'hard':
            hard()
        elif level == 'custom':
            custom()
        else:
            print(f"'{level}' is not a valid difficulty. Defaulting to easy.")
            easy()

    def generate(self):
        if self.diff_settings['word_count'] is None:
            self.diff_settings['word_count'] = 150

        words = self.faker.words(nb=self.diff_settings['word_count'])

        for i, word in enumerate(words):
            if self.diff_settings['numbers'] and random.random() < 0.1:
                words[i] = str(random.randint(0, 9999))
                continue

            if self.diff_settings['case_variation'] and random.random() < 0.15:
                words[i] = word.upper()
                continue

            if self.diff_settings['random_caps'] and random.random() < 0.05:
                words[i] = "".join(c.upper() if random.random() < 0.5 else c.lower() for c in word)

        text = " ".join(words)

        if self.diff_settings['capitalization'] and text:
            text = text[0].upper() + text[1:] + '.'

        self.current_text = text
        return self.current_text

def main():
    gen = Generator()
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        difficulty = sys.argv[1].lower()
        if difficulty in ['easy', 'medium', 'hard', 'custom']:
            gen.difficulty(difficulty)
        else:
            print(f"Invalid difficulty '{difficulty}'. Using 'easy' instead.")
            gen.difficulty('easy')
    else:
        # Interactive mode if no arguments provided
        print("Available difficulties: easy, medium, hard, custom")
        difficulty = input("Enter difficulty level (or press Enter for easy): ").strip().lower()
        if not difficulty:
            difficulty = 'easy'
        gen.difficulty(difficulty)
    
    print("\nGenerated text:")
    print(gen.generate())

# Example usage
if __name__ == "__main__":
    main()
