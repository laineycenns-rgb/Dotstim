# Random Dot Experiment
## Overview
This psychophysical experiment measures participants' ability to detect motion direction in a field of moving dots. Participants indicate whether a collection of moving dots moves left, right, or in some trials, neither, with those appearing as a collection of random directions. After each trial, participants rate their confidence in their response.

## Running the Experiment
### Step 1: Launch the Script
random_dot_motion_experiment.py
### Step 2: Dialog Box
Participant number: []
Age: []
Number of trials: Choose from 12, 60, 120, or 180 trials
### Step 3: On Screen Participant Name Entry  
Type first 4 letters of last name + last 2 digits of birth year (eg. ENNS03)  
Use BACKSPACE to delete mistakes  
Press RETURN when finished
### Step 4: Follow On-Screen Instructions  
The experiment will guide participants through the task.

## Experiment Design
### Trial Types:

#### Motion Trials:  
The dots move in a coherent pattern, either left or right. The experiment randomizes varying coherence levels across trials: 5%, 10%, 20%, 40%, and 80% coherence. 
#### Catch Trials:   
These catch trials appear equivalent to the trials per condition of the coherence levels (if it is a 12-trial experiment, there will be two trials per condition, including two for the catch condition). They have a 0% coherence level, making them appear as a sporadic collection of moving dots. This completely random motion test is in place to "catch" if the participants are guessing without reason. If one or both catch trials are incorrect, it can imply poor attention to the experiment and a random guessing approach. 

### Confidence Rating:
After each trial participants will be prompted to a screen asking for their subjective confidence in certainty for their response. The confidence rating can be applied in post hoc analyses for exploration of metacognition and the relation between subjective certainty and accuracy of their responses.

### Independent Variables

#### Coherence Level: 0.0, 0.1, 0.2, 0.4, 0.8 (proportion of dots moving in the same direction)
#### Direction: Left (180°) or Right (0°) (from center)

### Dependent Variables

#### Response: Participant's directional choice 
Response Keys:

LEFT arrow <-- Dots moving leftward  
RIGHT arrow --> Dots moving rightward  
SPACEBAR [] Random motion
#### Reaction Time: Time to make a directional response
#### Accuracy: Whether response matches the correct direction
#### Confidence Rating: Self-reported confidence   
1 = Not confident at all  
2 = Somewhat confident  
3 = Confident  
4 = Very confident
#### Confidence Reaction Time: Time to provide confidence rating

### Trial Structure

1. Fixation cross (0.5-1.5 seconds, randomized)
2. Dot motion display (until response)
3. Confidence rating screen (1-4)
4. Inter-trial interval (0.5 seconds)

#### 12 trials = 1 repetition × 6 coherence levels × 2 directions 
#### 60 trials = 5 repetitions × 6 coherence levels × 2 directions 
#### 120 trials = 10 repetitions × 6 coherence levels × 2 directions
#### 180 trials = 15 repetitions × 6 coherence levels × 2 directions

#### Data Output
File Format: Excel file (.xlsx)  
Filename: [P_name]_random_dot_motion.xlsx  
Your csv file will organize data like this:  
<img width="1398" height="227" alt="Screenshot 2025-10-23 at 4 16 31 PM" src="https://github.com/user-attachments/assets/0f94cb31-363e-41c0-97d6-3d67de518dc7" />

