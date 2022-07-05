#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.0),
    on July 03, 2022, at 04:21
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
expName = 'file6'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\mgreen\\gits\\psychopy-training-1-of-2\\psy\\file6\\file6_lastrun.py',
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
    size=[1920, 1080], fullscr=False, screen=0, 
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

# --- Initialize components for Routine "intro" ---
intro_text = visual.TextStim(win=win, name='intro_text',
    text="On each trial, you will be presented with a picture of an animal: either a cat or a dog.\n\nYour task is to identify the animal as quickly as possible, while avoiding errors, by pressing the 'c' key if it is a cat or the 'd' key if it is a dog.\n\nPress 'space' when you are ready to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_dismiss = keyboard.Keyboard()

# --- Initialize components for Routine "interval" ---
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# --- Initialize components for Routine "trial" ---
stimulus = visual.ImageStim(
    win=win,
    name='stimulus', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
response = keyboard.Keyboard()

# --- Initialize components for Routine "feedback" ---
wrong = visual.TextStim(win=win, name='wrong',
    text='WRONG!!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
right = visual.TextStim(win=win, name='right',
    text='CORRECT!!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
timedout = visual.TextStim(win=win, name='timedout',
    text='Time out - please respond faster!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from code
timer=core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "intro" ---
continueRoutine = True
# update component parameters for each repeat
intro_dismiss.keys = []
intro_dismiss.rt = []
_intro_dismiss_allKeys = []
# keep track of which components have finished
introComponents = [intro_text, intro_dismiss]
for thisComponent in introComponents:
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

# --- Run Routine "intro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_text* updates
    if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.tStart = t  # local t and not account for scr refresh
        intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_text.started')
        intro_text.setAutoDraw(True)
    
    # *intro_dismiss* updates
    waitOnFlip = False
    if intro_dismiss.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_dismiss.frameNStart = frameN  # exact frame index
        intro_dismiss.tStart = t  # local t and not account for scr refresh
        intro_dismiss.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_dismiss, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_dismiss.started')
        intro_dismiss.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_dismiss.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_dismiss.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_dismiss.status == STARTED and not waitOnFlip:
        theseKeys = intro_dismiss.getKeys(keyList=['space'], waitRelease=False)
        _intro_dismiss_allKeys.extend(theseKeys)
        if len(_intro_dismiss_allKeys):
            intro_dismiss.keys = _intro_dismiss_allKeys[-1].name  # just the last key pressed
            intro_dismiss.rt = _intro_dismiss_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro" ---
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_dismiss.keys in ['', [], None]:  # No response was made
    intro_dismiss.keys = None
thisExp.addData('intro_dismiss.keys',intro_dismiss.keys)
if intro_dismiss.keys != None:  # we had a response
    thisExp.addData('intro_dismiss.rt', intro_dismiss.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_sequence.xlsx'),
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
    
    # --- Prepare to start Routine "interval" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    intervalComponents = [ISI]
    for thisComponent in intervalComponents:
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
    
    # --- Run Routine "interval" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('ISI.started', t)
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            # Updating other components during *ISI*
            stimulus.setImage(animal_image)
            # Component updates done
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "interval" ---
    for thisComponent in intervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    trialComponents = [stimulus, response]
    for thisComponent in trialComponents:
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
    
    # --- Run Routine "trial" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulus* updates
        if stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus.frameNStart = frameN  # exact frame index
            stimulus.tStart = t  # local t and not account for scr refresh
            stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimulus.started')
            stimulus.setAutoDraw(True)
        if stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                stimulus.tStop = t  # not accounting for scr refresh
                stimulus.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus.stopped')
                stimulus.setAutoDraw(False)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response.started')
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                response.tStop = t  # not accounting for scr refresh
                response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response.stopped')
                response.status = FINISHED
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['c','d'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # was this correct?
                if (response.keys == str(expected_answer)) or (response.keys == expected_answer):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(expected_answer).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    t0=timer.getTime()
    # keep track of which components have finished
    feedbackComponents = [wrong, right, timedout]
    for thisComponent in feedbackComponents:
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
    
    # --- Run Routine "feedback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wrong* updates
        if wrong.status == NOT_STARTED and response.keys is not None and response.corr==0:
            # keep track of start time/frame for later
            wrong.frameNStart = frameN  # exact frame index
            wrong.tStart = t  # local t and not account for scr refresh
            wrong.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wrong, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wrong.started')
            wrong.setAutoDraw(True)
        if wrong.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wrong.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                wrong.tStop = t  # not accounting for scr refresh
                wrong.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wrong.stopped')
                wrong.setAutoDraw(False)
        
        # *right* updates
        if right.status == NOT_STARTED and response.keys is not None and response.corr==1:
            # keep track of start time/frame for later
            right.frameNStart = frameN  # exact frame index
            right.tStart = t  # local t and not account for scr refresh
            right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right.started')
            right.setAutoDraw(True)
        if right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                right.tStop = t  # not accounting for scr refresh
                right.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right.stopped')
                right.setAutoDraw(False)
        
        # *timedout* updates
        if timedout.status == NOT_STARTED and response.keys is None:
            # keep track of start time/frame for later
            timedout.frameNStart = frameN  # exact frame index
            timedout.tStart = t  # local t and not account for scr refresh
            timedout.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timedout, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'timedout.started')
            timedout.setAutoDraw(True)
        if timedout.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timedout.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                timedout.tStop = t  # not accounting for scr refresh
                timedout.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'timedout.stopped')
                timedout.setAutoDraw(False)
        # Run 'Each Frame' code from code
        t1=timer.getTime()
        elapsed=t1-t0
        if elapsed>2:
            continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
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
