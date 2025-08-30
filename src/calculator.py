from difflib import SequenceMatcher

class Calculator:
    
    def __init__(self):
        self.wpm = None
        self.accuracy = None
        self.error_count = None
        self.character_count = None
        
    def calculate_wpm(self, typed_text, time_elapsed):
        """Calculate Words Per Minute"""
        # Input validation
        if not isinstance(typed_text, str):
            return 0
        if time_elapsed <= 0:
            return 0
        
        character_count = len(typed_text)
        words = character_count / 5
        minutes = time_elapsed / 60
        
        self.wpm = round(words / minutes, 2) if minutes > 0 else 0
        return self.wpm
    
    def calculate_accuracy(self, original_text, typed_text):
        """Calculate typing accuracy percentage"""
        if not isinstance(original_text, str) or not isinstance(typed_text, str):
            return 0
            
        if len(original_text) == 0:
            return 100 if len(typed_text) == 0 else 0

        matcher = SequenceMatcher(None, original_text, typed_text)
        similarity = matcher.ratio()
        
        self.accuracy = round(similarity * 100, 2)
        return self.accuracy
    
    def count_errors(self, original_text, typed_text):
        """Count the number of typing errors"""
        if not isinstance(original_text, str) or not isinstance(typed_text, str):
            self.error_count = 0
            return self.error_count
            
        errors = 0
        min_length = min(len(original_text), len(typed_text))
        
        for i in range(min_length):
            if original_text[i] != typed_text[i]:
                errors += 1
        
        errors += abs(len(original_text) - len(typed_text))
        
        self.error_count = errors
        return self.error_count
    
    def get_typing_stats(self, original_text, typed_text, time_elapsed):
        """Get all typing statistics at once"""
        wpm = self.calculate_wpm(typed_text, time_elapsed)
        accuracy = self.calculate_accuracy(original_text, typed_text)
        errors = self.count_errors(original_text, typed_text)
        
        return {
            'wpm': wpm,
            'accuracy': accuracy,
            'errors': errors,
            'characters_typed': len(typed_text),
            'time_taken': time_elapsed
        }
    
    def calculate_net_wpm(self, typed_text, time_elapsed, original_text=None, error_penalty=True):
        """Calculate net WPM (accounting for errors)"""

        if time_elapsed <= 0:
            return 0
            
        gross_wpm = self.calculate_wpm(typed_text, time_elapsed)
        
        if error_penalty:
            if self.error_count is None and original_text is not None:
                self.count_errors(original_text, typed_text)

            if self.error_count is not None:
                net_wpm = max(0, gross_wpm - self.error_count)
                return round(net_wpm, 2)
        
        return gross_wpm
    
    def reset_stats(self):
        """Reset all calculated statistics"""
        self.wpm = None
        self.accuracy = None
        self.error_count = None
        self.character_count = None
    
    def format_stats_display(self, stats):
        """Format statistics for display"""
        return (
            f"WPM: {stats['wpm']}\n"
            f"Accuracy: {stats['accuracy']}%\n"
            f"Errors: {stats['errors']}\n"
            f"Characters Typed: {stats['characters_typed']}\n"
            f"Time Taken: {stats['time_taken']:.1f}s"
        )
    
    def get_performance_grade(self, wpm, accuracy):
        """Get a letter grade based on performance"""
        if accuracy < 80:
            return 'F'  
        elif wpm >= 60 and accuracy >= 95:
            return 'A+'
        elif wpm >= 50 and accuracy >= 90:
            return 'A'
        elif wpm >= 40 and accuracy >= 85:
            return 'B'
        elif wpm >= 30 and accuracy >= 80:
            return 'C'
        else:
            return 'D'

if __name__ == "__main__":
    calc = Calculator()
    
    original = "hello world test"
    typed = "hello wrold test"
    time_taken = 10.0

    print("Testing individual methods:")
    print(f"WPM: {calc.calculate_wpm(typed, time_taken)}")
    print(f"Accuracy: {calc.calculate_accuracy(original, typed)}")
    print(f"Errors: {calc.count_errors(original, typed)}")
    print(f"Net WPM: {calc.calculate_net_wpm(typed, time_taken, original)}")
    
    print("\nTesting comprehensive stats:")
    stats = calc.get_typing_stats(original, typed, time_taken)
    print(calc.format_stats_display(stats))

    print(f"\nBefore reset - WPM: {calc.wpm}")
    calc.reset_stats()
    print(f"After reset - WPM: {calc.wpm}")

    grade = calc.get_performance_grade(stats['wpm'], stats['accuracy'])
    print(f"Performance Grade: {grade}")