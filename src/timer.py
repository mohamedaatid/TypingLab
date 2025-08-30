import time

class Timer:
    def __init__(self):
        self.start_time = None  # Fixed: renamed to avoid conflict
        self.end_time = None    # Fixed: renamed to avoid conflict
        self.is_running = False
    
    def start_timer(self):
        """Start the timer"""
        self.start_time = time.time()
        self.is_running = True
        self.end_time = None  # Reset end time
    
    def stop_timer(self):
        """Stop the timer"""
        if not self.is_running:
            print("Warning: Timer was not running")
            return
            
        self.end_time = time.time()
        self.is_running = False
    
    def get_elapsed(self):
        """Get elapsed time in seconds"""
        if self.start_time is None:
            return 0  
        if self.is_running:
            return time.time() - self.start_time
        elif self.end_time is not None:
            
            return self.end_time - self.start_time
        else:
            return 0
    
    def reset(self):
        """Reset the timer"""
        self.start_time = None
        self.end_time = None
        self.is_running = False
    
    def get_formatted_time(self):
        """Get elapsed time formatted as MM:SS"""
        elapsed = self.get_elapsed()
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def is_timer_running(self):
        """Check if timer is currently running"""
        return self.is_running

if __name__ == "__main__":
    timer = Timer()
    
    print("Testing timer...")
    timer.start_timer()
    print("Timer started")

    time.sleep(2)
    
    print(f"Elapsed (while running): {timer.get_elapsed():.2f} seconds")
    
    timer.stop_timer()
    print(f"Final elapsed time: {timer.get_elapsed():.2f} seconds")
    print(f"Formatted time: {timer.get_formatted_time()}")