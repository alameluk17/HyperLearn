# HyperLearn
Learning disabilities refer to academic skill deficiencies in areas of reading, maths, and/or writing. ADHD is another high-incidence disorder occurring in approximately 5% of the population. The defining criteria for ADHD diagnosis involve the presence and severity of a significant number of symptoms, either in the area of inattention (e.g., easily distracted) or hyperactivity and impulsivity (e.g., often interrupts or intrudes).

Mobile/web applications are constantly increasing and people are trying to find solutions to problems in their daily life in the digital world. Addressing learning difficulties through mobile / web applications and gamified learning would be very effective for children with LD's and ADHD. The proposed solution is to develop a gamified educational platform that provides visual and auditory stimuli to enhance learning and motivation. This platform aims to help children with learning disabilities improve their understanding of language, numbers, and direction, through a reward system that keeps them engaged and motivated.


## HyperLearn - A Gamified Desktop Application for children with LDs and ADHD

HyperLearn can be viewed as a supplementary tool for children with learning disabilities. The incorporation of personalised adaptive learning techniques (Parental Control) , multi-sensory stimulation (Visual and Auditory) , positive reinforcement (Celebratory cartoons and scoring system) and accessibility design (Desktop application), creates an engaging and inclusive learning experience
Our application includes three games - Image Recognition, Safari and SpellBee. It includes a login page, where required credentials need to be entered to login/signup and on clicking the "SUBMIT" Button, the application is redirected to the home page which displays the User details: Score, Name and Age , and the games provided by the application.

Image Recognition game - Language and pronounciation of words are practiced via this game. The image of, say a lion is drawn on the game window and correspondingly the word, here lion, is displayed on the screen. On pressing the "RECORD" button , the child's voice is recognized (Python's speech-to-text module, Speech Recognition Pydub), corresponding messages are displayed.

Safari - It is a game developed to familiarize children with different animal sounds. The image of the animal is rendered on the window and a sound is played. If the displayed animal makes the sound that is played, "CORRECT" button is to be clicked, otherwise "WRONG". Corresponding messages are displayed.

SpellBee - Created to get children to practice their words and spellings. The word to be practiced is spelt out first by Python's text-to-speech module, pyttsx3 and later the child is required to fill in the blank spaces from the list of jumbled letters to form the word. Corresponding messages are displayed.

The directory consists of several audio (.mp3) and image (.jpeg, .png, .gif) files that would be rendered into the respective game windows.

## Instructions

1.Run 'pip -r install requirements.txt' on the terminal to install all the required python dependencies.

2.Run 'py loginpage.py' and 'py homepage.py' to render the application's login and home pages respectively

3.Run 'py imagerecognition.py' to play the image recognition game.

4.Run 'py animal.py' to play Safari.

5.Run 'py spellingGame.py' to play Spell Bee.

Note: Appropriate sound effects are rendered across all game windows.

### Credits

This project was developed as a part of an 18-hour hackathon, CodeHer, by [alameluk17](https://github.com/alameluk17), [hmae004](https://github.com/hmae004) & [jahnavimurali](https://github.com/jahnavimurali) 
