import sys
import random
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

        self.technical_words = [
            'algorithm', 'database', 'encryption', 'framework', 'implementation',
            'optimization', 'synchronization', 'authentication', 'configuration',
            'initialization', 'architecture', 'methodology', 'infrastructure'
        ]
        
        self.long_terms = [
            'comprehensive', 'extraordinary', 'revolutionary', 'unprecedented',
            'magnificent', 'overwhelming', 'transformational', 'incomprehensible',
            'international', 'developmental', 'constitutional', 'organizational'
        ]

    def difficulty(self, level):

        def easy():
            self.diff_settings['word_count'] = 150
            for key in self.diff_settings:
                if key != 'word_count':
                    self.diff_settings[key] = False

        def medium():
            self.diff_settings['word_count'] = 175 
            self.diff_settings['capitalization'] = True
            self.diff_settings['case_variation'] = True
            self.diff_settings['numbers'] = True
            self.diff_settings['punctuation'] = True
            # Reset unused settings
            self.diff_settings['random_caps'] = False
            self.diff_settings['technical_words'] = False
            self.diff_settings['long_terms'] = False

        def hard():
            self.diff_settings['word_count'] = 225
            self.diff_settings['capitalization'] = True
            self.diff_settings['case_variation'] = True
            self.diff_settings['random_caps'] = True
            self.diff_settings['technical_words'] = True
            self.diff_settings['long_terms'] = True
            self.diff_settings['numbers'] = True
            self.diff_settings['punctuation'] = True
            
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
            self.diff_settings['technical_words'] = get_bool("Include technical words?")
            self.diff_settings['long_terms'] = get_bool("Include long terms?")
            self.diff_settings['punctuation'] = get_bool("Include punctuation?")

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
            # Replace with numbers (10% chance)
            if self.diff_settings['numbers'] and random.random() < 0.1:
                words[i] = str(random.randint(0, 9999))
                continue
            
            if self.diff_settings['technical_words'] and random.random() < 0.08:
                words[i] = random.choice(self.technical_words)
                word = words[i]  # Update word for further transformations
            
            if self.diff_settings['long_terms'] and random.random() < 0.05:
                words[i] = random.choice(self.long_terms)
                word = words[i]  # Update word for further transformations
            
            if self.diff_settings['random_caps'] and random.random() < 0.05:
                words[i] = "".join(c.upper() if random.random() < 0.5 else c.lower() for c in word)
            elif self.diff_settings['case_variation'] and random.random() < 0.15:
                words[i] = word.upper()

        text = " ".join(words)
        
        if self.diff_settings['punctuation']:
            text = self._add_punctuation(text)

        if self.diff_settings['capitalization'] and text:
            if self.diff_settings['punctuation']:
                sentences = text.split('. ')
                sentences = [s.strip() for s in sentences if s.strip()]
                capitalized_sentences = []
                for sentence in sentences:
                    if sentence:
                        capitalized_sentences.append(sentence[0].upper() + sentence[1:] if len(sentence) > 1 else sentence.upper())
                text = '. '.join(capitalized_sentences)
                if not text.endswith('.'):
                    text += '.'
            else:
                text = text[0].upper() + text[1:] + '.'

        self.current_text = text
        return self.current_text
    
    def _add_punctuation(self, text):
        """Add punctuation to the text"""
        words = text.split()
        result = []
        
        for i, word in enumerate(words):
            result.append(word)
            
            if random.random() < 0.05 and i < len(words) - 1:
                result[-1] += ','
            
            elif random.random() < 0.08 and i > 5 and i < len(words) - 3:
                result[-1] += '.'
        
        return " ".join(result)
    
    def get_current_settings(self):
        """Return current difficulty settings for debugging"""
        return self.diff_settings.copy()
    
    def get_text_stats(self):
        """Return statistics about the current generated text"""
        if not self.current_text:
            return None
            
        return {
            'character_count': len(self.current_text),
            'word_count': len(self.current_text.split()),
            'has_punctuation': any(c in self.current_text for c in '.,!?;:'),
            'has_numbers': any(c.isdigit() for c in self.current_text),
            'has_capitals': any(c.isupper() for c in self.current_text)
        }

def main():
    gen = Generator()

    if len(sys.argv) > 1:
        difficulty = sys.argv[1].lower()
        if difficulty in ['easy', 'medium', 'hard', 'custom']:
            gen.difficulty(difficulty)
        else:
            print(f"Invalid difficulty '{difficulty}'. Using 'easy' instead.")
            gen.difficulty('easy')
    else:
        print("Available difficulties: easy, medium, hard, custom")
        difficulty = input("Enter difficulty level (or press Enter for easy): ").strip().lower()
        if not difficulty:
            difficulty = 'easy'
        gen.difficulty(difficulty)
    
    print("\nGenerated text:")
    generated_text = gen.generate()
    print(generated_text)
    
    stats = gen.get_text_stats()
    if stats:
        print(f"\nText Statistics:")
        print(f"Characters: {stats['character_count']}")
        print(f"Words: {stats['word_count']}")
        print(f"Has punctuation: {stats['has_punctuation']}")
        print(f"Has numbers: {stats['has_numbers']}")
        print(f"Has capitals: {stats['has_capitals']}")

if __name__ == "__main__":
    main()