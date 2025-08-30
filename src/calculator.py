import time
from difflib import SequenceMatcher

class Calculator:
    
    def __init__(self):
        self.wpm = None
        self.accuracy = None
        self.error_count = None
        self.character_count = None
        
    def calculate_wpm(self, typed_text, time_elapsed):
        """Calculate Words Per Minute"""
        if time_elapsed <= 0:
            return 0
        
        # Count characters (including spaces) and divide by 5 (standard word length)
        character_count = len(typed_text)
        words = character_count / 5
        minutes = time_elapsed / 60
        
        self.wpm = round(words / minutes, 2) if minutes > 0 else 0
        return self.wpm
    
    def calculate_accuracy(self, original_text, typed_text):
        """Calculate typing accuracy percentage"""
        if len(original_text) == 0:
            return 100
        
        # Use difflib to compare texts
        matcher = SequenceMatcher(None, original_text, typed_text)
        similarity = matcher.ratio()
        
        self.accuracy = round(similarity * 100, 2)
        return self.accuracy
    
    def count_errors(self, original_text, typed_text):
        """Count the number of typing errors"""
        errors = 0
        min_length = min(len(original_text), len(typed_text))
        
        # Count character mismatches
        for i in range(min_length):
            if original_text[i] != typed_text[i]:
                errors += 1
        
        # Add errors for length differences
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
    
    def calculate_net_wpm(self, typed_text, time_elapsed, error_penalty=True):
        """Calculate net WPM (accounting for errors)"""
        gross_wpm = self.calculate_wpm(typed_text, time_elapsed)
        
        if error_penalty and self.error_count:
            # Subtract errors from gross WPM
            net_wpm = max(0, gross_wpm - self.error_count)
            return round(net_wpm, 2)
        
        return gross_wpm