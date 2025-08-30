# TypingLab

A comprehensive typing practice application built in Python that helps users improve their typing speed and accuracy through customizable difficulty levels and detailed performance analytics.

## Features

- **Multiple Difficulty Levels**: Easy, Medium, Hard, and Custom configurations
- **Real-time Performance Tracking**: WPM, accuracy, error count, and net WPM calculations
- **Customizable Text Generation**: Various challenges including numbers, capitalization, technical terms
- **Detailed Statistics**: Comprehensive performance metrics and feedback
- **Command Line Interface**: Easy-to-use interactive experience

## Project Structure

TypingLab/   
├── main.py            
├── .gitignore            
├── src/
│   ├── __pycache__/      
│   ├── __init__.py
│   ├── timer.py
│   ├── textGenerator.py
│   ├── calculator.py
├── requirements.txt
└── README.md

## dependencies:
```bash
pip install faker
```
## Usage:
```bash
python main.py
```
### You can also run individual modules for testing:
```bash
# Test text generator with specific difficulty
python src/textGenerator.py easy
python src/textGenerator.py medium
python src/textGenerator.py hard
python src/textGenerator.py custom

# Test calculator functionality
python src/calculator.py

# Test timer functionality
python src/timer.py
```
## How It Works
### Text Generation (textGenerator.py)
The Generator class creates practice text with customizable difficulty:
```
Difficulty Levels:

Easy: 150 words, basic lowercase text
Medium: 175 words, includes capitalization, numbers, and punctuation
Hard: 225 words, includes all features: random caps, technical terms, long words
Custom: User-defined settings for all parameters
```
#### Features:

Random word generation using Faker library
Technical vocabulary injection
Number substitution (0-9999 range)
Various capitalization patterns
Punctuation insertion
Long/complex terms

### Timer Functionality (timer.py)
The Timer class handles precise time tracking:
#### Methods:
```
start_timer(): Begins timing
stop_timer(): Ends timing
get_elapsed(): Returns elapsed time in seconds
reset(): Resets timer state
get_formatted_time(): Returns time as MM:SS format
```
#### Features:

Real-time elapsed time calculation
State tracking (running/stopped)
Error handling for improper usage
Formatted time display

## Statistics Calculator (calculator.py)
The Calculator class computes typing performance metrics:
Metrics Calculated:

WPM (Words Per Minute): Characters ÷ 5 ÷ minutes
Accuracy: Percentage similarity using difflib
Error Count: Character mismatches + length differences
Net WPM: Gross WPM minus error penalty

### Methods:
```
calculate_wpm(): Basic speed calculation
calculate_accuracy(): Precision measurement
count_errors(): Error detection and counting
get_typing_stats(): Comprehensive statistics bundle
calculate_net_wpm(): Speed adjusted for errors
reset_stats(): Clear previous calculations
```
## Main Application (main.py)
The TypingLab class orchestrates the complete typing test experience:
### Workflow:

User selects difficulty level
Text is generated based on settings
Timer starts when user begins typing
Input is captured and timer stops
Statistics are calculated and displayed
Performance feedback is provided

### Features:

Interactive difficulty selection
Real-time typing interface
Comprehensive results display
Performance grading system
Option to retake tests