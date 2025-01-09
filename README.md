# Flag Quiz Game
## Introduction
The Flag Guessing Game is an interactive and educational web-based game designed to test and enhance geographic knowledge. Players identify the country corresponding to a displayed flag, with randomized options and score tracking to make it both engaging and challenging. The game also features a nostalgic old DOS-style interface, giving it a retro aesthetic that stands out.

## Problem Domain
In today’s globalized world, geographic knowledge is essential, but many people find it challenging to remember country flags. Traditional methods of learning geography can often feel dull and uninspiring.

### Key Problems:
Lack of engaging tools to learn country flags.
Difficulty retaining geographic knowledge.
Limited interactive educational games with retro design appeal.

## Solution Domain
The Flag Guessing Game offers an innovative solution by providing a fun, interactive platform to learn and test flag knowledge. With dynamic gameplay, real-time score updates, and a nostalgic user interface, the game combines education with entertainment.

### Key Features:
Displays a random flag for each round.
Provides multiple-choice options, including randomized distractors.
Tracks scores and rounds in real-time.
Designed with a retro aesthetic for a unique visual experience.

##Requirements
###Software Requirements
Python 3.7 or higher
Flask
HTML, CSS, and JavaScript
Web browser (Google Chrome, Mozilla Firefox, etc.)
###Hardware Requirements
System with 4GB RAM (minimum)
Stable internet connection for hosting (optional if run locally)
500MB disk space for storing flag images and code

##Data Structure Used
The primary data structure used in the project includes:

List: To store the names of countries and flags, enabling efficient random sampling and option generation.
Dictionary: For mapping countries to their respective flags for easy retrieval.
Set: To ensure options for each round are unique.

## Preview
[Watch the video](https://github.com/viveksethaliya/Flags-quiz/blob/bb872f6039e3d5ace82e818aad12bae342b06645/video.mp4)


# Flag Guessing Game

## Introduction
The Flag Guessing Game is an interactive and educational web-based game designed to test and enhance geographic knowledge. Players identify the country corresponding to a displayed flag, with randomized options and score tracking to make it both engaging and challenging. The game also features a nostalgic **old DOS-style interface**, giving it a retro aesthetic that stands out.

---

## Problem Domain
In today’s globalized world, geographic knowledge is essential, but many people find it challenging to remember country flags. Traditional methods of learning geography can often feel dull and uninspiring.

### Key Problems:
- Lack of engaging tools to learn country flags.
- Difficulty retaining geographic knowledge.
- Limited interactive educational games with retro design appeal.

---

## Solution Domain
The Flag Guessing Game offers an innovative solution by providing a fun, interactive platform to learn and test flag knowledge. With dynamic gameplay, real-time score updates, and a nostalgic user interface, the game combines education with entertainment.

### Key Features:
- Displays a random flag for each round.
- Provides multiple-choice options, including randomized distractors.
- Tracks scores and rounds in real-time.
- Designed with a retro aesthetic for a unique visual experience.

---

## Requirements

### Software Requirements
- Python 3.7 or higher
- Flask
- HTML, CSS, and JavaScript
- Web browser (Google Chrome, Mozilla Firefox, etc.)

### Hardware Requirements
- System with 4GB RAM (minimum)
- Stable internet connection for hosting (optional if run locally)
- 500MB disk space for storing flag images and code

---

## Data Structure Used
The primary data structures used in the project include:
- **List**: To store the names of countries and flags, enabling efficient random sampling and option generation.
- **Dictionary**: For mapping countries to their respective flags for easy retrieval.
- **Set**: To ensure options for each round are unique.

---

## Methodology

### 1. Random Flag Selection
- A flag is randomly chosen from the dataset (list of countries and flag files).
- Three random distractors are generated, ensuring they are not duplicates of the correct answer.

### 2. Gameplay Logic
- The selected flag is displayed, and multiple-choice options are presented.
- The player selects an option, and the system checks if the answer is correct.
- The score is updated based on correct guesses, and the next round begins.

### 3. Frontend Interface
- Designed with a retro blue-and-gray DOS-style aesthetic.
- Score and round information are dynamically updated on the screen.

### 4. Backend Logic
- Built with Flask to handle game routing and serve static flag images.
- API endpoints for generating rounds and validating answers.

---

### Screenshot
![Flag Guessing Game Screenshot](screenshot.png)  
*Example of the gameplay interface with a flag and options displayed.*

---

## Summary/Conclusion
The Flag Guessing Game successfully blends education and entertainment to create an engaging platform for learning geography. Its retro design appeals to nostalgia, while its modern web-based implementation ensures accessibility. This project demonstrates the integration of frontend and backend technologies to deliver a seamless user experience.

### Future Enhancements:
- Add difficulty levels (e.g., based on regions or number of options).
- Implement a database to track high scores across sessions.
- Introduce a timed mode for added challenge.

---


