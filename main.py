from src.timer import Timer 
from src.textGenerator import Generator  
from src.calculator import Calculator

class TypingLab:
    
    def __init__(self):
        self.timer = Timer()        
        self.text_gen = Generator() 
        self.calc = Calculator()
        
    def run_test(self):
        """Main typing test flow"""
        try:
            print("Welcome to TypingLab!")
            print("Available difficulties: easy, medium, hard, custom")
            
            difficulty = input("Choose difficulty (or press Enter for easy): ").strip().lower()
            if not difficulty:
                difficulty = 'easy'
                
            valid_difficulties = ['easy', 'medium', 'hard', 'custom']
            if difficulty not in valid_difficulties:
                print(f"Invalid difficulty '{difficulty}'. Using 'easy' instead.")
                difficulty = 'easy'
            
            self.text_gen.difficulty(difficulty)
            
            test_text = self.text_gen.generate()
            
            if not test_text:
                print("Error: Could not generate text. Please try again.")
                return
            
            print("\n" + "="*50)
            print("Type the following text:")
            print("="*50)
            print(test_text)
            print("="*50)
            print("Press Enter when ready, then start typing...")
            input()
            
            self.timer.start_timer() 
            
            print("START TYPING NOW:")
            typed_text = input()
            
            self.timer.stop_timer()   
            
            time_taken = self.timer.get_elapsed() 
            
            if time_taken <= 0:
                print("Error: Invalid time measurement. Please try again.")
                return
                
            stats = self.calc.get_typing_stats(test_text, typed_text, time_taken)
            
            self.show_results(stats, test_text, typed_text)
            
        except KeyboardInterrupt:
            print("\n\nTest interrupted by user.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")
        
    def show_results(self, stats, original_text=None, typed_text=None):
        """Display test results"""
        print("\n" + "="*30)
        print("TYPING TEST RESULTS")
        print("="*30)
        print(f"Time: {stats['time_taken']:.2f} seconds")
        print(f"WPM: {stats['wpm']}")
        print(f"Accuracy: {stats['accuracy']}%")
        print(f"Errors: {stats['errors']}")
        print(f"Characters Typed: {stats['characters_typed']}")
        
        if original_text and typed_text:
            net_wpm = self.calc.calculate_net_wpm(typed_text, stats['time_taken'], original_text, error_penalty=True)
            print(f"Net WPM: {net_wpm}")

        self.show_feedback(stats)
        
    def show_feedback(self, stats):
        """Provide performance feedback"""
        print("\n" + "-"*20)
        print("PERFORMANCE FEEDBACK")
        print("-"*20)
        
        if stats['wpm'] >= 60:
            print("🎉 Excellent typing speed!")
        elif stats['wpm'] >= 40:
            print("👍 Good typing speed!")
        elif stats['wpm'] >= 25:
            print("📈 Keep practicing to improve speed!")
        else:
            print("🎯 Focus on accuracy first, speed will come!")
            
        if stats['accuracy'] >= 95:
            print("🎯 Outstanding accuracy!")
        elif stats['accuracy'] >= 85:
            print("✅ Good accuracy!")
        elif stats['accuracy'] >= 75:
            print("⚠️ Work on reducing errors")
        else:
            print("🔄 Focus on accuracy over speed")
        
    def run(self):
        """Main entry point"""
        try:
            while True:
                self.run_test()
                
                again = input("\nTake another test? (y/n): ").lower().strip()
                if again not in ['y', 'yes']:
                    print("Thanks for using TypingLab!")
                    break
                    
                self.calc.reset_stats()
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")

def main():
    app = TypingLab()
    app.run()

if __name__ == "__main__":
    main()