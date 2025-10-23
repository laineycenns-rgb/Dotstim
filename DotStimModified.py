import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy import visual, core
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data
import random
### DIALOG BOX ROUTINE ###
exp_info = {'participant_nr': '', 'age': '','number of trials':[12,60,120,180]} #since 6 conditions changed trials to be evenly divisable by 12 (multiplied by 5, 10, and 15)
#drop down menu
dlg = DlgFromDict(exp_info)
trialn= exp_info['number of trials']

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1200, 800), fullscr=False, monitor='samsung')

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=False)

# Initialize a (global) clock
clock = Clock()

# Initialize Keyboard
kb = Keyboard()
kb.clearEvents()

### WELCOME ROUTINE ###
# Create a welcome screen and show for 2 seconds
welcome_txt_stim = TextStim(win, text="Welcome to the Dot Stimulation Experiment!", color=(1, 0, 0), font='Calibri')
welcome_txt_stim.draw()
win.flip()
wait(2)

## collect participant number again
instruct_txt = """ 
Please type the first four letters of your last name followed by the last two digits of your birth year. 
When you are finished, hit the return key.
"""
instruct=TextStim(win,instruct_txt,pos=(0,0.5))
instruct.draw()
win.flip()
# Initialize keyboard and wait for response
kb = Keyboard()
p_name=''
while True:
    keys = kb.getKeys()
    #collects each key pressed
    for key in keys:
        if key.name == 'backspace':
            p_name = p_name[:-1] 
        else:
            p_name = p_name + key.name  
    if 'return' in keys:
            p_name=p_name[:-6]
            break
        
    display = TextStim(win, p_name)
    display.draw()
    instruct.draw()
    win.flip()
        

### INSTRUCTION ROUTINE ###
task_instruct_txt = """ 
In this experiment, you will see a collection of moving dots on the screen.

On each trial the predominant movement of the dots will either be towards the left of the screen, 
the right of the screen 
or both appearing as a random collection of moving dots.

You should indicate with the arrow keys (left or right) for which direction the motion is in and if it is both press the spacebar.

Sometimes it can be hard to tell! Pay attention and go with your instinct!

Press return to begin...
    
 """

# Show instructions and wait until response (return)
task_instruct_txt = TextStim(win, task_instruct_txt, alignText='left', font='Calibri', height=0.085)
task_instruct_txt.draw()
win.flip()

# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'return' in keys:
        break  # break out of the loop!

# Configuration parameters
# parameter is a variable that you are changing in the experiment
N_TRIALS = trialn
N_DOTS = 150
DOT_SIZE = 5  # in pixels
DOT_SPEED = 0.5  # degrees/frame
DOT_FIELD_SIZE = 2  # degrees
COHERENCE_LEVELS = [0.00, 0.05, 0.1, 0.2, 0.4, 0.8]  # Added 0.00 as a coherence catch trial to measure attention and chance of guessing
DIRECTIONS = [0, 180]  # Right (0°) and Left (180°)
FIXATION_MIN = 0.5  # seconds
FIXATION_MAX = 1.5  # fixation cross

# Create fixation and dots stimuli once (more efficient)
fix = TextStim(win, "+", height=2)
dots = DotStim(
    win, #projection
    fieldShape='circle', #shape
    nDots=N_DOTS, #150 dots
    fieldSize=DOT_FIELD_SIZE, 
    dotSize=DOT_SIZE,
    speed=DOT_SPEED,
    dotLife=-1,  # infinite lifetime
    noiseDots='direction', # noise to dot motion
    signalDots='same' # one core direction
)

# New confidence rating stimulus
confidence_txt = """
How confident are you in your response?

Press a number key from 1 to 4:

1 = Not confident at all
2 = Somewhat confident
3 = Confident
4 = Very confident
"""
confidence_stim = TextStim(win, confidence_txt, color=(1, 0, 0), font='Calibri', height=0.1)

# Create trial handler for proper randomization and data collection
trial_list = []

for coherence in COHERENCE_LEVELS: #for every value in this coherence levels do...
    for direction in DIRECTIONS: #for every value in directions do something else
        # Multiple repetitions of each condition
        for rep in range(0,int(trialn)//12): 
        # adjusted to account for 6 conditions
        # for catch trials (0 coherence) correct response is 'none'
            if coherence == 0.0:
                correct_resp = 'none'
            else:
                correct_resp = 'left' if direction == 180 else 'right'
            
            trial_list.append({
                'coherence': coherence,
                'direction': direction,
                'correct_response': correct_resp,
                'trial_type': 'catch' if coherence == 0.0 else 'motion'
            }) 

# replacing random.shuffle function
trials = data.TrialHandler(trial_list, nReps=1, method='random')
# Main experiment loop
for trial in trials:
    # Variable fixation period (prevents anticipation)
    fixation_time = random.uniform(FIXATION_MIN, FIXATION_MAX)
    # random time between the fixation min and max determined in parameters (between 0.5 and 1.5)
    # random.uniform is every number has an equal chance of being drawn
    # gausian distribution is a bell curve where there is not an equal distribution
    
    # Show fixation
    fix.draw()
    win.flip()
    wait(fixation_time)
    
    # Set dot parameters for this trial
    dots.coherence = trial['coherence'] 
    dots.dir = trial['direction'] 
    
    # Reset keyboard and clock
    kb.clock.reset()
    kb.clearEvents()
    
    # Present dots and collect response
    response = None
    rt = None
    
    while response is None:
        dots.draw()
        win.flip()
        
        # Check for response
        keys = kb.getKeys(['left', 'right', 'space', 'escape'], waitRelease=False) # added space for catch conditions
        if keys:
            response = keys[0].name #first key was pressed and name
            rt = keys[0].rt #first key was pressed and rt
            
            # Allow escape to quit
            if response == 'escape': 
                win.close()
                quit()
           
           # if space is pressed response will be recorded as 'none'
            if response == 'space':
                response = 'none'

# Now present confidence ratings stim

    kb.clock.reset()
    kb.clearEvents()
    confidence = None
    confidence_rt = None

    while confidence is None:
        confidence_stim.draw()
        win.flip()
        keys = kb.getKeys(['1', '2', '3', '4', 'escape'], waitRelease=False)
        if keys:
            confidence = keys[0].name
            confidence_rt = keys[0].rt
                
            if confidence == 'escape':
                win.close()
                quit()
    
    # Record trial data
    trials.addData('response', response) 
    trials.addData('rt', rt)
    trials.addData('correct', response == trial['correct_response'])
    trials.addData('confidence', int(confidence)) #save confidence rating as the key integer pressed
    trials.addData('confidence_rt', confidence_rt)
    trials.addData('fixation_duration', fixation_time)
    
    # Brief inter-trial interval
    win.flip()
    wait(0.5)

# Save data
filename = p_name + '_random_dot_motion'
trials.saveAsExcel(filename + '.xlsx')

# Show completion message
end_text = visual.TextStim(win, "That is the end of the experiment! Thank you!", color=(1, 0, 0), height=0.1)
end_text.draw()
win.flip()
core.wait(3)

win.close()
core.quit()







