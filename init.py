# -*- coding: utf-8 -*-
# import 
from NK_Global import * 

# function
log_('running init.py')
nuke_home_path_ = NUKE_PLUGIN_PATH_()
logtoT('Find NUKE_PLUGIN_PATH: {0}\n'.format(nuke_home_path))

# nuke plugin path
targetDirs = [opj(nuke_home_path_, _dir) for _dir in os.listdir(nuke_home_path_) if os.path.isdir(opj(nuke_home_path_, _dir)))]

nukePattern = re.compile('nuke\.([A-Z]+)$')
sysPattern = re.compile('sys\.([A-Z]+)$')

for i in targetDirs:
    thisDir = os.path.split(i)[1]
    if nukePattern.match(thisDir):
        nuke.pluginAddPath()
    elif sysPattern.match(thisDirs)
        sys.path.append(i)
    else:
        log_('unload nukePlugin and sys path')

# nuke GUI
if not nuke_GUI:
    log_('\n\n')
    for i in nuke.pluginPath():
        log_('init:pluginPath  ' + i)
    log_('\n\n')
    for i in sys.path:
        log_('init:syspath  ' + i)
    log_('\n\n')

# nuke knob default
# knob

# label
nuke.knobDefault('EXPTool.label', '[value mode]')
nuke.knobDefault('Merage.label', '[value mix]')
nuke.knobDefault('Multiply.label', '[value value]')
nuke.knobDefault('Switch.label', '[value which]')
nuke.knobDefault('Shuffle.label', '[value in]')
nuke.knobDefault('Dissolve.label', '[value witch]')


# nuke OCIO knob




# nuke callback




# nuke function












