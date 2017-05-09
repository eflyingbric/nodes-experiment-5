#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Tue  9 May 20:11:57 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'connectNodes'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/elo/Documents/nodes-experiment-5/connectNodes.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
SIZE = (100)
OF = (15)
SCREENSIZE = (1440,900)
welcome = visual.TextStim(win=win, name='welcome',
    text='Welcome!',
    font='Arial',
    pos=(0, 0), height=100, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
instruct = visual.TextStim(win=win, name='instruct',
    text='This task is about reuniting 2 robots together by combining shapes to make a pathway.\n\n',
    font='Arial',
    pos=[0,0], height=50, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
rob0 = visual.ImageStim(
    win=win, name='rob0',
    image='robot1.png', mask=None,
    ori=0, pos=(-250, -100), size=200,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
robb = visual.ImageStim(
    win=win, name='robb',
    image='robot1.png', mask=None,
    ori=0, pos=(250, -100), size=200,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
na = visual.Polygon(
    win=win, name='na',
    edges=90, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='blue', lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
nb = visual.Polygon(
    win=win, name='nb',
    edges=90, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='blue', lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
nc = visual.Polygon(
    win=win, name='nc',
    edges=90, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='blue', lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
s1 = visual.Rect(
    win=win, name='s1',
    width=(110, 40)[0], height=(110, 40)[1],
    ori=0, pos=(-110, -100),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
s2 = visual.Rect(
    win=win, name='s2',
    width=(110,40)[0], height=(110,40)[1],
    ori=0, pos=(0,-100),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
s3 = visual.Rect(
    win=win, name='s3',
    width=(110,40)[0], height=(110,40)[1],
    ori=0, pos=(110,-100),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
heart = visual.ImageStim(
    win=win, name='heart',
    image='heart.png', mask=None,
    ori=0, pos=(0, -100), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "example"
exampleClock = core.Clock()
SIZE = (100)
OF = (15)
SCREENSIZE = (1440,900)

xshift = 250

# ROW 1 (TOP)
LOC1 = (-(2*SIZE)-(2*OF) + xshift, 2*SIZE+2*OF)
LOC2 = (-SIZE-OF + xshift, 2*SIZE+2*OF)
LOC3 = (0 + xshift, 2*SIZE+2*OF)
LOC4 = (SIZE+OF + xshift, 2*SIZE+2*OF)
LOC5 = (2*SIZE+2*OF + xshift, 2*SIZE+2*OF)

# ROW 2
LOC6 = (-(2*SIZE)-(2*OF)+xshift, SIZE+OF)
LOC7 = (-SIZE-OF+xshift, SIZE+OF)
LOC8 = (0+xshift, SIZE+OF)
LOC9 = (SIZE+OF+xshift, SIZE+OF)
LOC10 = (2*SIZE+2*OF+xshift, SIZE+OF)

# ROW 3
LOC11 = (-(2*SIZE)-(2*OF)+xshift, 0)
LOC12 = (-SIZE-OF+xshift, 0)
LOC13 = (0+xshift, 0)
LOC14 = (SIZE+OF+xshift, 0)
LOC15 = (2*SIZE+2*OF+xshift, 0)

# ROW 4
LOC16 = (-(2*SIZE)-(2*OF)+xshift, -SIZE-OF)
LOC17 = (-SIZE-OF+xshift, -SIZE-OF)
LOC18 = (0+xshift, -SIZE-OF)
LOC19 = (SIZE+OF+xshift, -SIZE-OF)
LOC20 = (2*SIZE+2*OF+xshift, -SIZE-OF)

# ROW 5 (BOTTOM)
LOC21 = (-(2*SIZE)-(2*OF)+xshift, -(2*SIZE)-(2*OF))
LOC22 = (-SIZE-OF+xshift, -(2*SIZE)-(2*OF))
LOC23 = (0+xshift, -(2*SIZE)-(2*OF))
LOC24 = (SIZE+OF+xshift, -(2*SIZE)-(2*OF))
LOC25 = (2*SIZE+2*OF+xshift, -(2*SIZE)-(2*OF))
text_2 = visual.TextStim(win=win, name='text_2',
    text="Let's take an example",
    font='Arial',
    pos=[0,0], height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
nod1 = visual.Polygon(
    win=win, name='nod1',
    edges=90, size=SIZE,
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
nod2 = visual.Polygon(
    win=win, name='nod2',
    edges=90, size=SIZE,
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
nod3 = visual.Polygon(
    win=win, name='nod3',
    edges=90, size=SIZE,
    ori=0, pos=LOC7,
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
nod4 = visual.Polygon(
    win=win, name='nod4',
    edges=90, size=SIZE,
    ori=0, pos=LOC8,
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
rob1 = visual.ImageStim(
    win=win, name='rob1',
    image='robot1.png', mask=None,
    ori=1.0, pos=LOC16, size=SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
rob2 = visual.ImageStim(
    win=win, name='rob2',
    image='sin', mask=None,
    ori=0, pos=LOC9, size=SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
sh1 = visual.Rect(
    win=win, name='sh1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=LOC11,
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
sh2a = visual.Rect(
    win=win, name='sh2a',
    width=(60, 40)[0], height=(60, 40)[1],
    ori=0, pos=(50,113),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
sh2b = visual.Rect(
    win=win, name='sh2b',
    width=(40, 80)[0], height=(40, 80)[1],
    ori=0, pos=(22, 93),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
sh3 = visual.Rect(
    win=win, name='sh3',
    width=(110, 40)[0], height=(110, 40)[1],
    ori=0, pos=LOC7,
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
sh4 = visual.Rect(
    win=win, name='sh4',
    width=(110, 40)[0], height=(110, 40)[1],
    ori=0, pos=LOC8,
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)

# Initialize components for Routine "start"
startClock = core.Clock()
star = visual.TextStim(win=win, name='star',
    text='Now, when you are ready press the space bar to start the experiment\n',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Robot Icon from
# www.iconarchive.com/show/outline-icons-by-iconsmind/Robot-2-icon.html

#Set size for a node and and offset btw nodes:
SIZE = (100)
OF = (15)
SCREENSIZE = (1440,900)

LEFTPANEL_SIZE = (800,SCREENSIZE[1])
LEFTPANEL_LOCATION = (-SCREENSIZE[0]/4-LEFTPANEL_SIZE[0]/2+200, 0)

# Selection image (with shapes and keys) size is:
SELIMG = (500,250)
# For a better fit you can rescale it:
scaleby = 0.5
SISIZE = (SELIMG[0]*scaleby, SELIMG[1]*scaleby)

#Locations:
#Set up all possible locations for nodes for them to be later
#recycled. This is for a 5x5 grid:

# to shift the below grid on x axis adjust this value
xshift = 250

# ROW 1 (TOP)
LOC1 = (-(2*SIZE)-(2*OF) + xshift, 2*SIZE+2*OF)
LOC2 = (-SIZE-OF + xshift, 2*SIZE+2*OF)
LOC3 = (0 + xshift, 2*SIZE+2*OF)
LOC4 = (SIZE+OF + xshift, 2*SIZE+2*OF)
LOC5 = (2*SIZE+2*OF + xshift, 2*SIZE+2*OF)

# ROW 2
LOC6 = (-(2*SIZE)-(2*OF)+xshift, SIZE+OF)
LOC7 = (-SIZE-OF+xshift, SIZE+OF)
LOC8 = (0+xshift, SIZE+OF)
LOC9 = (SIZE+OF+xshift, SIZE+OF)
LOC10 = (2*SIZE+2*OF+xshift, SIZE+OF)

# ROW 3
LOC11 = (-(2*SIZE)-(2*OF)+xshift, 0)
LOC12 = (-SIZE-OF+xshift, 0)
LOC13 = (0+xshift, 0)
LOC14 = (SIZE+OF+xshift, 0)
LOC15 = (2*SIZE+2*OF+xshift, 0)

# ROW 4
LOC16 = (-(2*SIZE)-(2*OF)+xshift, -SIZE-OF)
LOC17 = (-SIZE-OF+xshift, -SIZE-OF)
LOC18 = (0+xshift, -SIZE-OF)
LOC19 = (SIZE+OF+xshift, -SIZE-OF)
LOC20 = (2*SIZE+2*OF+xshift, -SIZE-OF)

# ROW 5 (BOTTOM)
LOC21 = (-(2*SIZE)-(2*OF)+xshift, -(2*SIZE)-(2*OF))
LOC22 = (-SIZE-OF+xshift, -(2*SIZE)-(2*OF))
LOC23 = (0+xshift, -(2*SIZE)-(2*OF))
LOC24 = (SIZE+OF+xshift, -(2*SIZE)-(2*OF))
LOC25 = (2*SIZE+2*OF+xshift, -(2*SIZE)-(2*OF))

# Locations of the selection items
sx = -630
S1LOC = (sx,0)
S2LOC = (sx,-120)
S3LOC = (sx,-240)
S4LOC = (sx,-360)

# Locations for selection lables
stx = -400
S1TXTLOC = (stx, -80)
S2TXTLOC = (stx, -200)
S3TXTLOC = (stx, -320)
S4TXTLOC = (stx, -440)
whitebackground = visual.Rect(
    win=win, name='whitebackground',
    width=LEFTPANEL_SIZE[0], height=LEFTPANEL_SIZE[1],
    ori=0, pos=LEFTPANEL_LOCATION,
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
robotS = visual.ImageStim(
    win=win, name='robotS',
    image='robot1.png', mask=None,
    ori=0, pos=[0,0], size=SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
node1 = visual.Polygon(
    win=win, name='node1',
    edges=90, size=SIZE,
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
node2 = visual.Polygon(
    win=win, name='node2',
    edges=90, size=SIZE,
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
node3 = visual.Polygon(
    win=win, name='node3',
    edges=90, size=SIZE,
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
node4 = visual.Polygon(
    win=win, name='node4',
    edges=90, size=SIZE,
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
node5 = visual.Polygon(
    win=win, name='node5',
    edges=90, size=SIZE,
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
robotF = visual.ImageStim(
    win=win, name='robotF',
    image='robot1.png', mask=None,
    ori=0, pos=[0,0], size=SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
select1 = visual.Polygon(
    win=win, name='select1',
    edges=90, size=SIZE,
    ori=0, pos=S1LOC,
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
select2 = visual.Polygon(
    win=win, name='select2',
    edges=90, size=SIZE,
    ori=0, pos=S2LOC,
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
select3 = visual.Polygon(
    win=win, name='select3',
    edges=90, size=SIZE,
    ori=0, pos=S3LOC,
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
select4 = visual.Polygon(
    win=win, name='select4',
    edges=90, size=SIZE,
    ori=0, pos=S4LOC,
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
selection = visual.ImageStim(
    win=win, name='selection',units='pix', 
    image='mastershapes.png', mask=None,
    ori=0, pos=[0,0], size=(500,400),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
sel = visual.TextStim(win=win, name='sel',
    text=u'Press keys A, B, C, D to \nselect the shape you associate \nwith each colour. Think carefully, you only have one choice!',
    font=u'Arial',
    pos=(-450, 250), height=(30), wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-15.0);

# Initialize components for Routine "Eval"
EvalClock = core.Clock()
# ROW 1 (TOP)
LOC1 = (-(2*SIZE)-(2*OF) + xshift, 2*SIZE+2*OF)
LOC2 = (-SIZE-OF + xshift, 2*SIZE+2*OF)
LOC3 = (0 + xshift, 2*SIZE+2*OF)
LOC4 = (SIZE+OF + xshift, 2*SIZE+2*OF)
LOC5 = (2*SIZE+2*OF + xshift, 2*SIZE+2*OF)

# ROW 2
LOC6 = (-(2*SIZE)-(2*OF)+xshift, SIZE+OF)
LOC7 = (-SIZE-OF+xshift, SIZE+OF)
LOC8 = (0+xshift, SIZE+OF)
LOC9 = (SIZE+OF+xshift, SIZE+OF)
LOC10 = (2*SIZE+2*OF+xshift, SIZE+OF)

# ROW 3
LOC11 = (-(2*SIZE)-(2*OF)+xshift, 0)
LOC12 = (-SIZE-OF+xshift, 0)
LOC13 = (0+xshift, 0)
LOC14 = (SIZE+OF+xshift, 0)
LOC15 = (2*SIZE+2*OF+xshift, 0)

# ROW 4
LOC16 = (-(2*SIZE)-(2*OF)+xshift, -SIZE-OF)
LOC17 = (-SIZE-OF+xshift, -SIZE-OF)
LOC18 = (0+xshift, -SIZE-OF)
LOC19 = (SIZE+OF+xshift, -SIZE-OF)
LOC20 = (2*SIZE+2*OF+xshift, -SIZE-OF)

# ROW 5 (BOTTOM)
LOC21 = (-(2*SIZE)-(2*OF)+xshift, -(2*SIZE)-(2*OF))
LOC22 = (-SIZE-OF+xshift, -(2*SIZE)-(2*OF))
LOC23 = (0+xshift, -(2*SIZE)-(2*OF))
LOC24 = (SIZE+OF+xshift, -(2*SIZE)-(2*OF))
LOC25 = (2*SIZE+2*OF+xshift, -(2*SIZE)-(2*OF))

msg = ''

Evaluation = visual.TextStim(win=win, name='Evaluation',
    text=u'Based on what you know, is this pathway correct? \n',
    font=u'Arial',
    pos=(0, 300), height=40, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);
polygon = visual.Polygon(
    win=win, name='polygon',
    edges=90, size=(100),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',
    edges=90, size=100,
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_3 = visual.Polygon(
    win=win, name='polygon_3',
    edges=90, size=(100),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
polygon_4 = visual.Polygon(
    win=win, name='polygon_4',
    edges=90, size=(100),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
polygon_5 = visual.Polygon(
    win=win, name='polygon_5',
    edges=90, size=(100),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
choice = visual.TextStim(win=win, name='choice',
    text='default text',
    font='Arial',
    pos=(0, -300), height=50, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
ro = visual.ImageStim(
    win=win, name='ro',
    image='robot1.png', mask=None,
    ori=0, pos=[0,0], size=(100),
    color=1.0, colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
rq = visual.ImageStim(
    win=win, name='rq',
    image='robot1.png', mask=None,
    ori=0, pos=[0,0], size=(100),
    color=1.0, colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)

# Initialize components for Routine "feeback"
feebackClock = core.Clock()
msg = ""

feedback = visual.TextStim(win=win, name='feedback',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Thank_you"
Thank_youClock = core.Clock()
thankyou = visual.TextStim(win=win, name='thankyou',
    text='Thank you for your participation.\n',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(18.000000)
# update component parameters for each repeat

instruct.setPos((0, 150))
na.setPos((-110,-100))
na.setSize(SIZE)
nb.setPos((0,-100))
nb.setSize(SIZE)
nc.setPos((110,-100))
nc.setSize(SIZE)
# keep track of which components have finished
InstructionsComponents = [welcome, instruct, rob0, robb, na, nb, nc, s1, s2, s3, heart]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *welcome* updates
    if t >= 0.0 and welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome.tStart = t
        welcome.frameNStart = frameN  # exact frame index
        welcome.setAutoDraw(True)
    frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if welcome.status == STARTED and t >= frameRemains:
        welcome.setAutoDraw(False)
    
    # *instruct* updates
    if t >= 3.0 and instruct.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct.tStart = t
        instruct.frameNStart = frameN  # exact frame index
        instruct.setAutoDraw(True)
    frameRemains = 3.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instruct.status == STARTED and t >= frameRemains:
        instruct.setAutoDraw(False)
    
    # *rob0* updates
    if t >= 6.0 and rob0.status == NOT_STARTED:
        # keep track of start time/frame for later
        rob0.tStart = t
        rob0.frameNStart = frameN  # exact frame index
        rob0.setAutoDraw(True)
    frameRemains = 6.0 + 12- win.monitorFramePeriod * 0.75  # most of one frame period left
    if rob0.status == STARTED and t >= frameRemains:
        rob0.setAutoDraw(False)
    
    # *robb* updates
    if t >= 6.0 and robb.status == NOT_STARTED:
        # keep track of start time/frame for later
        robb.tStart = t
        robb.frameNStart = frameN  # exact frame index
        robb.setAutoDraw(True)
    frameRemains = 6.0 + 12- win.monitorFramePeriod * 0.75  # most of one frame period left
    if robb.status == STARTED and t >= frameRemains:
        robb.setAutoDraw(False)
    
    # *na* updates
    if t >= 6.5 and na.status == NOT_STARTED:
        # keep track of start time/frame for later
        na.tStart = t
        na.frameNStart = frameN  # exact frame index
        na.setAutoDraw(True)
    frameRemains = 6.5 + 7.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if na.status == STARTED and t >= frameRemains:
        na.setAutoDraw(False)
    
    # *nb* updates
    if t >= 7 and nb.status == NOT_STARTED:
        # keep track of start time/frame for later
        nb.tStart = t
        nb.frameNStart = frameN  # exact frame index
        nb.setAutoDraw(True)
    frameRemains = 7 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
    if nb.status == STARTED and t >= frameRemains:
        nb.setAutoDraw(False)
    
    # *nc* updates
    if t >= 7.5 and nc.status == NOT_STARTED:
        # keep track of start time/frame for later
        nc.tStart = t
        nc.frameNStart = frameN  # exact frame index
        nc.setAutoDraw(True)
    frameRemains = 7.5 + 6.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if nc.status == STARTED and t >= frameRemains:
        nc.setAutoDraw(False)
    
    # *s1* updates
    if t >= 8.5 and s1.status == NOT_STARTED:
        # keep track of start time/frame for later
        s1.tStart = t
        s1.frameNStart = frameN  # exact frame index
        s1.setAutoDraw(True)
    frameRemains = 8.5 + 5.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if s1.status == STARTED and t >= frameRemains:
        s1.setAutoDraw(False)
    
    # *s2* updates
    if t >= 9.5 and s2.status == NOT_STARTED:
        # keep track of start time/frame for later
        s2.tStart = t
        s2.frameNStart = frameN  # exact frame index
        s2.setAutoDraw(True)
    frameRemains = 9.5 + 4.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if s2.status == STARTED and t >= frameRemains:
        s2.setAutoDraw(False)
    
    # *s3* updates
    if t >= 10.5 and s3.status == NOT_STARTED:
        # keep track of start time/frame for later
        s3.tStart = t
        s3.frameNStart = frameN  # exact frame index
        s3.setAutoDraw(True)
    frameRemains = 10.5 + 3.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if s3.status == STARTED and t >= frameRemains:
        s3.setAutoDraw(False)
    
    # *heart* updates
    if t >= 14 and heart.status == NOT_STARTED:
        # keep track of start time/frame for later
        heart.tStart = t
        heart.frameNStart = frameN  # exact frame index
        heart.setAutoDraw(True)
    frameRemains = 14 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if heart.status == STARTED and t >= frameRemains:
        heart.setAutoDraw(False)
    if heart.status == STARTED:  # only update if drawing
        heart.setSize(200+50*sin(t), log=False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "example"-------
t = 0
exampleClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

text_2.setPos((-300, 300))
nod1.setFillColor('red')
nod1.setPos(LOC11)
nod2.setFillColor('yellow')
nod2.setPos(LOC6)
nod2.setLineColor('yellow')
nod3.setFillColor('blue')
nod3.setLineColor('blue')
nod4.setFillColor('blue')
nod4.setLineColor('blue')
rob1.setOri(0)
rob2.setImage('robot1.png')
key_resp_2 = event.BuilderKeyResponse()
sh1.setSize((40,110))
# keep track of which components have finished
exampleComponents = [text_2, nod1, nod2, nod3, nod4, rob1, rob2, key_resp_2, sh1, sh2a, sh2b, sh3, sh4]
for thisComponent in exampleComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "example"-------
while continueRoutine:
    # get current time
    t = exampleClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *nod1* updates
    if t >= 0.0 and nod1.status == NOT_STARTED:
        # keep track of start time/frame for later
        nod1.tStart = t
        nod1.frameNStart = frameN  # exact frame index
        nod1.setAutoDraw(True)
    
    # *nod2* updates
    if t >= 0.0 and nod2.status == NOT_STARTED:
        # keep track of start time/frame for later
        nod2.tStart = t
        nod2.frameNStart = frameN  # exact frame index
        nod2.setAutoDraw(True)
    
    # *nod3* updates
    if t >= 0.0 and nod3.status == NOT_STARTED:
        # keep track of start time/frame for later
        nod3.tStart = t
        nod3.frameNStart = frameN  # exact frame index
        nod3.setAutoDraw(True)
    
    # *nod4* updates
    if t >= 0.0 and nod4.status == NOT_STARTED:
        # keep track of start time/frame for later
        nod4.tStart = t
        nod4.frameNStart = frameN  # exact frame index
        nod4.setAutoDraw(True)
    
    # *rob1* updates
    if t >= 0.0 and rob1.status == NOT_STARTED:
        # keep track of start time/frame for later
        rob1.tStart = t
        rob1.frameNStart = frameN  # exact frame index
        rob1.setAutoDraw(True)
    
    # *rob2* updates
    if t >= 0.0 and rob2.status == NOT_STARTED:
        # keep track of start time/frame for later
        rob2.tStart = t
        rob2.frameNStart = frameN  # exact frame index
        rob2.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *sh1* updates
    if t >= 2.0 and sh1.status == NOT_STARTED:
        # keep track of start time/frame for later
        sh1.tStart = t
        sh1.frameNStart = frameN  # exact frame index
        sh1.setAutoDraw(True)
    
    # *sh2a* updates
    if t >= 2.5 and sh2a.status == NOT_STARTED:
        # keep track of start time/frame for later
        sh2a.tStart = t
        sh2a.frameNStart = frameN  # exact frame index
        sh2a.setAutoDraw(True)
    
    # *sh2b* updates
    if t >= 2.5 and sh2b.status == NOT_STARTED:
        # keep track of start time/frame for later
        sh2b.tStart = t
        sh2b.frameNStart = frameN  # exact frame index
        sh2b.setAutoDraw(True)
    
    # *sh3* updates
    if t >= 3.0 and sh3.status == NOT_STARTED:
        # keep track of start time/frame for later
        sh3.tStart = t
        sh3.frameNStart = frameN  # exact frame index
        sh3.setAutoDraw(True)
    
    # *sh4* updates
    if t >= 3.5 and sh4.status == NOT_STARTED:
        # keep track of start time/frame for later
        sh4.tStart = t
        sh4.frameNStart = frameN  # exact frame index
        sh4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "example"-------
for thisComponent in exampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "example" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
startComponents = [star, key_resp_4]
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *star* updates
    if t >= 0.0 and star.status == NOT_STARTED:
        # keep track of start time/frame for later
        star.tStart = t
        star.frameNStart = frameN  # exact frame index
        star.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('designs.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    resp1 = event.BuilderKeyResponse()
    corrAnswer1 = 'a'
    corrAnswer2 = 'b'
    corrAnswer3 = 'c'
    corrAnswer4 = 'd'
    robotS.setPos(eval(rs))
    node1.setFillColor(n1col)
    node1.setPos(eval(n1))
    node2.setFillColor(n2col)
    node2.setPos(eval(n2))
    node3.setFillColor(n3col)
    node3.setPos(eval(n3))
    node4.setFillColor(n4col)
    node4.setPos(eval(n4))
    node5.setFillColor(n5col)
    node5.setPos(eval(n5))
    robotF.setPos(eval(re))
    # keep track of which components have finished
    trialComponents = [resp1, whitebackground, robotS, node1, node2, node3, node4, node5, robotF, select1, select2, select3, select4, selection, sel]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp1* updates
        if t >= 0 and resp1.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp1.tStart = t
            resp1.frameNStart = frameN  # exact frame index
            resp1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp1.clock.reset)  # t=0 on next screen flip
        if resp1.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 'b', 'c', 'd'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp1.keys.extend(theseKeys)  # storing all keys
                resp1.rt.append(resp1.clock.getTime())
        # Depending on how many response participant has made
        # the legend with the keys and shapes will move
        # if subject has made 4 response then the routine will end
        
        if len(resp1.keys) == 0:
            sloc = S1TXTLOC
        elif len(resp1.keys) == 1:
            # Change the location of the legend after each response
            sloc = S2TXTLOC
        elif len(resp1.keys) == 2:
            sloc = S3TXTLOC
        elif len(resp1.keys) == 3:
            sloc = S4TXTLOC
        elif len(resp1.keys) == 4:
            # If 4 responses have been made - end this routine
            continueRoutine = False
        
        # *whitebackground* updates
        if t >= 0.0 and whitebackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            whitebackground.tStart = t
            whitebackground.frameNStart = frameN  # exact frame index
            whitebackground.setAutoDraw(True)
        
        # *robotS* updates
        if t >= 0.0 and robotS.status == NOT_STARTED:
            # keep track of start time/frame for later
            robotS.tStart = t
            robotS.frameNStart = frameN  # exact frame index
            robotS.setAutoDraw(True)
        
        # *node1* updates
        if t >= 0.0 and node1.status == NOT_STARTED:
            # keep track of start time/frame for later
            node1.tStart = t
            node1.frameNStart = frameN  # exact frame index
            node1.setAutoDraw(True)
        
        # *node2* updates
        if t >= 0.0 and node2.status == NOT_STARTED:
            # keep track of start time/frame for later
            node2.tStart = t
            node2.frameNStart = frameN  # exact frame index
            node2.setAutoDraw(True)
        
        # *node3* updates
        if t >= 0.0 and node3.status == NOT_STARTED:
            # keep track of start time/frame for later
            node3.tStart = t
            node3.frameNStart = frameN  # exact frame index
            node3.setAutoDraw(True)
        
        # *node4* updates
        if t >= 0.0 and node4.status == NOT_STARTED:
            # keep track of start time/frame for later
            node4.tStart = t
            node4.frameNStart = frameN  # exact frame index
            node4.setAutoDraw(True)
        
        # *node5* updates
        if t >= 0.0 and node5.status == NOT_STARTED:
            # keep track of start time/frame for later
            node5.tStart = t
            node5.frameNStart = frameN  # exact frame index
            node5.setAutoDraw(True)
        
        # *robotF* updates
        if t >= 0.0 and robotF.status == NOT_STARTED:
            # keep track of start time/frame for later
            robotF.tStart = t
            robotF.frameNStart = frameN  # exact frame index
            robotF.setAutoDraw(True)
        
        # *select1* updates
        if t >= 0.0 and select1.status == NOT_STARTED:
            # keep track of start time/frame for later
            select1.tStart = t
            select1.frameNStart = frameN  # exact frame index
            select1.setAutoDraw(True)
        
        # *select2* updates
        if t >= 0.0 and select2.status == NOT_STARTED:
            # keep track of start time/frame for later
            select2.tStart = t
            select2.frameNStart = frameN  # exact frame index
            select2.setAutoDraw(True)
        
        # *select3* updates
        if t >= 0.0 and select3.status == NOT_STARTED:
            # keep track of start time/frame for later
            select3.tStart = t
            select3.frameNStart = frameN  # exact frame index
            select3.setAutoDraw(True)
        
        # *select4* updates
        if t >= 0.0 and select4.status == NOT_STARTED:
            # keep track of start time/frame for later
            select4.tStart = t
            select4.frameNStart = frameN  # exact frame index
            select4.setAutoDraw(True)
        
        # *selection* updates
        if t >= 0.0 and selection.status == NOT_STARTED:
            # keep track of start time/frame for later
            selection.tStart = t
            selection.frameNStart = frameN  # exact frame index
            selection.setAutoDraw(True)
        if selection.status == STARTED:  # only update if drawing
            selection.setOpacity(1, log=False)
            selection.setPos(sloc, log=False)
        
        # *sel* updates
        if t >= 0.0 and sel.status == NOT_STARTED:
            # keep track of start time/frame for later
            sel.tStart = t
            sel.frameNStart = frameN  # exact frame index
            sel.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp1.keys in ['', [], None]:  # No response was made
        resp1.keys=None
    trials.addData('resp1.keys',resp1.keys)
    if resp1.keys != None:  # we had a response
        trials.addData('resp1.rt', resp1.rt)
    '''
    At the end of each trial the below code will
    check which keys were pressed in what order
    then from that it constructs the 'correct' values
    what supposed to be pressed in in r1-r4 in the spreadsheet
    '''
    
    if resp1.keys[0] == r1:
        corrAnswer1 = 1
    else:
        corrAnswer1 = 0
    
    if resp1.keys[1] == r2:
        corrAnswer2 = 1
    else:
        corrAnswer2 = 0
    
    if resp1.keys[2] == r3:
        corrAnswer3 = 1
    else:
        corrAnswer3 = 0
    
    if resp1.keys[3] == r4:
        corrAnswer4 = 1
    else:
        corrAnswer4 = 0
    
    trials.addData('corrAnsw1',corrAnswer1)
    trials.addData('corrAnsw2',corrAnswer2)
    trials.addData('corrAnsw3',corrAnswer3)
    trials.addData('corrAnsw4',corrAnswer4)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('designs1.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    # ------Prepare to start Routine "Eval"-------
    t = 0
    EvalClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    
    polygon.setFillColor(n1col)
    polygon.setPos(eval(n1))
    polygon_2.setFillColor(n2col)
    polygon_2.setPos(eval(n2))
    polygon_3.setFillColor(n3col)
    polygon_3.setPos(eval(n3))
    polygon_4.setFillColor(n4col)
    polygon_4.setPos(eval(n4))
    polygon_5.setFillColor(n5col)
    polygon_5.setPos(eval(n5))
    choice.setText("Press 'y' for Yes  \nPress 'n' for No")
    ro.setColor([1,1,1], colorSpace='rgb')
    ro.setPos(eval(rs))
    rq.setColor([1,1,1], colorSpace='rgb')
    rq.setPos(eval(re))
    resp3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    EvalComponents = [Evaluation, polygon, polygon_2, polygon_3, polygon_4, polygon_5, choice, ro, rq, resp3]
    for thisComponent in EvalComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Eval"-------
    while continueRoutine:
        # get current time
        t = EvalClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Evaluation* updates
        if t >= 0.0 and Evaluation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Evaluation.tStart = t
            Evaluation.frameNStart = frameN  # exact frame index
            Evaluation.setAutoDraw(True)
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        
        # *polygon_2* updates
        if t >= 0.0 and polygon_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_2.tStart = t
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.setAutoDraw(True)
        
        # *polygon_3* updates
        if t >= 0.0 and polygon_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_3.tStart = t
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.setAutoDraw(True)
        
        # *polygon_4* updates
        if t >= 0.0 and polygon_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_4.tStart = t
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.setAutoDraw(True)
        
        # *polygon_5* updates
        if t >= 0.0 and polygon_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_5.tStart = t
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.setAutoDraw(True)
        
        # *choice* updates
        if t >= 0.0 and choice.status == NOT_STARTED:
            # keep track of start time/frame for later
            choice.tStart = t
            choice.frameNStart = frameN  # exact frame index
            choice.setAutoDraw(True)
        
        # *ro* updates
        if t >= 0.0 and ro.status == NOT_STARTED:
            # keep track of start time/frame for later
            ro.tStart = t
            ro.frameNStart = frameN  # exact frame index
            ro.setAutoDraw(True)
        
        # *rq* updates
        if t >= 0.0 and rq.status == NOT_STARTED:
            # keep track of start time/frame for later
            rq.tStart = t
            rq.frameNStart = frameN  # exact frame index
            rq.setAutoDraw(True)
        
        # *resp3* updates
        if t >= 0.5 and resp3.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp3.tStart = t
            resp3.frameNStart = frameN  # exact frame index
            resp3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp3.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp3.keys = theseKeys[-1]  # just the last key pressed
                resp3.rt = resp3.clock.getTime()
                # was this 'correct'?
                if (resp3.keys == str(corrAns)) or (resp3.keys == corrAns):
                    resp3.corr = 1
                else:
                    resp3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EvalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Eval"-------
    for thisComponent in EvalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    if resp3.keys == corrAns:
        msg="Fabulous!"
    else:
        msg="Oops, so sorry"
    
    if resp3.keys == corrAns:
        msg="Fabulous!"
    else:
        msg="Oops, so sorry"
    
    # check responses
    if resp3.keys in ['', [], None]:  # No response was made
        resp3.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp3.corr = 1  # correct non-response
        else:
           resp3.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('resp3.keys',resp3.keys)
    trials_2.addData('resp3.corr', resp3.corr)
    if resp3.keys != None:  # we had a response
        trials_2.addData('resp3.rt', resp3.rt)
    # the Routine "Eval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feeback"-------
    t = 0
    feebackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    if resp3.keys == corrAns:
        msg="Fabulous!"
    else:
        msg="Oops, sorry"
    
    if resp3.keys == corrAns:
        msg="Well done!"
    else:
        msg="Robots also divorce"
    
    feedback.setText(msg)
    # keep track of which components have finished
    feebackComponents = [feedback]
    for thisComponent in feebackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feeback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feebackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedback* updates
        if t >= 0.0 and feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback.tStart = t
            feedback.frameNStart = frameN  # exact frame index
            feedback.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback.status == STARTED and t >= frameRemains:
            feedback.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feebackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feeback"-------
    for thisComponent in feebackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Thank_you"-------
t = 0
Thank_youClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
Thank_youComponents = [thankyou]
for thisComponent in Thank_youComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thank_you"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Thank_youClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyou* updates
    if t >= 0.0 and thankyou.status == NOT_STARTED:
        # keep track of start time/frame for later
        thankyou.tStart = t
        thankyou.frameNStart = frameN  # exact frame index
        thankyou.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thankyou.status == STARTED and t >= frameRemains:
        thankyou.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_youComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thank_you"-------
for thisComponent in Thank_youComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
