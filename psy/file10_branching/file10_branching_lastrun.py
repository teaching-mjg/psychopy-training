#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.0),
    on July 07, 2022, at 19:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.0'
expName = 'file10_branching'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mgreen\\gits\\psychopy-training-1-of-2\\psy\\file10_branching\\file10_branching_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 800], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "choose" ---
# Run 'Begin Experiment' code from code
timer = core.Clock()
prompt = visual.TextStim(win=win, name='prompt',
    text='You will see some pictures of animals to rate for typicality.\nDo you prefer to see cats or dogs? Click on your preference.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
cats_option = visual.TextStim(win=win, name='cats_option',
    text='cats',
    font='Open Sans',
    pos=(-.2, -.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
dogs_option = visual.TextStim(win=win, name='dogs_option',
    text='dogs',
    font='Open Sans',
    pos=(0.2, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "cats" ---
text = visual.TextStim(win=win, name='text',
    text='Please rate for typicality',
    font='Open Sans',
    pos=(0, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
slider = visual.Slider(win=win, name='slider',
    startValue=3, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["atypical","","neutral","","typical"], ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=True, ori=0.0, depth=-2, readOnly=False)

# --- Initialize components for Routine "dogs" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='Please rate for typicality',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=3, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["atypical","","neutral","","typical"], ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=True, ori=0.0, depth=-2, readOnly=False)

# --- Initialize components for Routine "follow_up" ---
goodbye = visual.TextStim(win=win, name='goodbye',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
goodbye_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "choose" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from code
t0 = timer.getTime()
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
chooseComponents = [prompt, cats_option, dogs_option, mouse]
for thisComponent in chooseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "choose" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from code
    t1 = timer.getTime()
    elapsed_time = t1-t0
    if mouse.isPressedIn(cats_option):
        flag = "cats"
        input_xls = "cats.xlsx"
        nRepsCats=1
        nRepsDogs=0
        mouse_rt = elapsed_time
        thisExp.addData("mouse_rt", mouse_rt)
        mouse_selection = "cats"
        thisExp.addData("mouse_selection", mouse_selection)
        continueRoutine=False
    if mouse.isPressedIn(dogs_option):
        flag = "dogs"
        input_xls = "dogs.xlsx"
        nRepsCats=0
        nRepsDogs=1
        mouse_rt = elapsed_time
        thisExp.addData("mouse_rt", mouse_rt)
        mouse_selection = "dogs"
        thisExp.addData("mouse_selection", mouse_selection)
        continueRoutine = False
    
    
    # *prompt* updates
    if prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prompt.frameNStart = frameN  # exact frame index
        prompt.tStart = t  # local t and not account for scr refresh
        prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prompt.started')
        prompt.setAutoDraw(True)
    
    # *cats_option* updates
    if cats_option.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cats_option.frameNStart = frameN  # exact frame index
        cats_option.tStart = t  # local t and not account for scr refresh
        cats_option.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cats_option, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cats_option.started')
        cats_option.setAutoDraw(True)
    
    # *dogs_option* updates
    if dogs_option.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dogs_option.frameNStart = frameN  # exact frame index
        dogs_option.tStart = t  # local t and not account for scr refresh
        dogs_option.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dogs_option, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dogs_option.started')
        dogs_option.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([cats_option, dogs_option])
                    clickableList = [cats_option, dogs_option]
                except:
                    clickableList = [[cats_option, dogs_option]]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in chooseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "choose" ---
for thisComponent in chooseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.clicked_name', mouse.clicked_name)
thisExp.nextEntry()
# the Routine "choose" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    catloop = data.TrialHandler(nReps=nRepsCats, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(input_xls),
        seed=None, name='catloop')
    thisExp.addLoop(catloop)  # add the loop to the experiment
    thisCatloop = catloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCatloop.rgb)
    if thisCatloop != None:
        for paramName in thisCatloop:
            exec('{} = thisCatloop[paramName]'.format(paramName))
    
    for thisCatloop in catloop:
        currentLoop = catloop
        # abbreviate parameter names if possible (e.g. rgb = thisCatloop.rgb)
        if thisCatloop != None:
            for paramName in thisCatloop:
                exec('{} = thisCatloop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "cats" ---
        continueRoutine = True
        # update component parameters for each repeat
        image.setImage(animal_image)
        slider.reset()
        # keep track of which components have finished
        catsComponents = [text, image, slider]
        for thisComponent in catsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "cats" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                text.setAutoDraw(True)
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                image.setAutoDraw(True)
            
            # *slider* updates
            if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider.frameNStart = frameN  # exact frame index
                slider.tStart = t  # local t and not account for scr refresh
                slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider.started')
                slider.setAutoDraw(True)
            
            # Check slider for response to end routine
            if slider.getRating() is not None and slider.status == STARTED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in catsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cats" ---
        for thisComponent in catsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        catloop.addData('slider.response', slider.getRating())
        catloop.addData('slider.rt', slider.getRT())
        # the Routine "cats" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsCats repeats of 'catloop'
    
    
    # set up handler to look after randomisation of conditions etc
    dogloop = data.TrialHandler(nReps=nRepsDogs, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(input_xls),
        seed=None, name='dogloop')
    thisExp.addLoop(dogloop)  # add the loop to the experiment
    thisDogloop = dogloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDogloop.rgb)
    if thisDogloop != None:
        for paramName in thisDogloop:
            exec('{} = thisDogloop[paramName]'.format(paramName))
    
    for thisDogloop in dogloop:
        currentLoop = dogloop
        # abbreviate parameter names if possible (e.g. rgb = thisDogloop.rgb)
        if thisDogloop != None:
            for paramName in thisDogloop:
                exec('{} = thisDogloop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "dogs" ---
        continueRoutine = True
        # update component parameters for each repeat
        image_2.setImage(animal_image)
        slider_2.reset()
        # keep track of which components have finished
        dogsComponents = [text_2, image_2, slider_2]
        for thisComponent in dogsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "dogs" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                text_2.setAutoDraw(True)
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.started')
                image_2.setAutoDraw(True)
            
            # *slider_2* updates
            if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_2.frameNStart = frameN  # exact frame index
                slider_2.tStart = t  # local t and not account for scr refresh
                slider_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_2.started')
                slider_2.setAutoDraw(True)
            
            # Check slider_2 for response to end routine
            if slider_2.getRating() is not None and slider_2.status == STARTED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in dogsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "dogs" ---
        for thisComponent in dogsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        dogloop.addData('slider_2.response', slider_2.getRating())
        dogloop.addData('slider_2.rt', slider_2.getRT())
        # the Routine "dogs" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsDogs repeats of 'dogloop'
    
    
    # --- Prepare to start Routine "follow_up" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from set_follow
    followup_text = "Thanks for taking part."+\
    "Press any key to be sent to the wikipedia page for " +\
    str(flag)
    
    
    goodbye.setText(followup_text)
    goodbye_resp.keys = []
    goodbye_resp.rt = []
    _goodbye_resp_allKeys = []
    # keep track of which components have finished
    follow_upComponents = [goodbye, goodbye_resp]
    for thisComponent in follow_upComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "follow_up" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *goodbye* updates
        if goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye.frameNStart = frameN  # exact frame index
            goodbye.tStart = t  # local t and not account for scr refresh
            goodbye.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye.started')
            goodbye.setAutoDraw(True)
        
        # *goodbye_resp* updates
        waitOnFlip = False
        if goodbye_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_resp.frameNStart = frameN  # exact frame index
            goodbye_resp.tStart = t  # local t and not account for scr refresh
            goodbye_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye_resp.started')
            goodbye_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(goodbye_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(goodbye_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if goodbye_resp.status == STARTED and not waitOnFlip:
            theseKeys = goodbye_resp.getKeys(keyList=None, waitRelease=False)
            _goodbye_resp_allKeys.extend(theseKeys)
            if len(_goodbye_resp_allKeys):
                goodbye_resp.keys = _goodbye_resp_allKeys[-1].name  # just the last key pressed
                goodbye_resp.rt = _goodbye_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in follow_upComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "follow_up" ---
    for thisComponent in follow_upComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from set_follow
    import webbrowser
    if flag == "cats":
        url = 'https://en.wikipedia.org/wiki/Cat'
    if flag == "dogs":
        url = 'https://en.wikipedia.org/wiki/Dog'
    webbrowser.open(url)
    # check responses
    if goodbye_resp.keys in ['', [], None]:  # No response was made
        goodbye_resp.keys = None
    trials.addData('goodbye_resp.keys',goodbye_resp.keys)
    if goodbye_resp.keys != None:  # we had a response
        trials.addData('goodbye_resp.rt', goodbye_resp.rt)
    # the Routine "follow_up" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
