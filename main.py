from src.timer import timer
from src.text_generator import generator
from src.calculator import Calculator

class TypingLab:
    
    def __init__(self):
        self.timer = timer()
        self.text_gen = generator()
        self.calc = Calculator()
        
    def run_test(self):
        """Main typing test flow"""
        print("Welcome to TypingLab!")
        print("Available difficulties: easy, medium, hard, custom")
        
        # Get difficulty choice
        difficulty = input("Choose difficulty (or press Enter for easy): ").strip().lower()
        if not difficulty:
            difficulty = 'easy'
            
        # Set up text generator
        self.text_gen.difficulty(difficulty)
        
        # Generate text
        test_text = self.text_gen.generate()
        
        print("\n" + "="*50)
        print("Type the following text:")
        print("="*50)
        print(test_text)
        print("="*50)
        print("Press Enter when ready, then start typing...")
        input()
        
        # Start timing
        self.timer.start_timer()
        
        # Get user input
        print("START TYPING NOW:")
        typed_text = input()
        
        # Stop timing
        self.timer.stop_timer()
        
        # Calculate results
        time_taken = self.timer.get_elapsed()
        stats = self.calc.get_typing_stats(test_text, typed_text, time_taken)
        
        # Display results
        self.show_results(stats)
        
    def show_results(self, stats):
        """Display test results"""
        print("\n" + "="*30)
        print("TYPING TEST RESULTS")
        print("="*30)
        print(f"Time: {stats['time_taken']:.2f} seconds")
        print(f"WPM: {stats['wpm']}")
        print(f"Accuracy: {stats['accuracy']}%")
        print(f"Errors: {stats['errors']}")
        print(f"Characters Typed: {stats['characters_typed']}")
        
    def run(self):
        """Main entry point"""
        while True:
            self.run_test()
            
            again = input("\nTake another test? (y/n): ").lower().strip()
            if again not in ['y', 'yes']:
                print("Thanks for using TypingLab!")
                break

def main():
    app = TypingLab()
    app.run()

if __name__ == "__main__":
    main()